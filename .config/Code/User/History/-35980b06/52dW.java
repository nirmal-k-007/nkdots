
public class LaptopClient {
    
    private static final CopyOnWriteArraySet<ChatServer> connections = new CopyOnWriteArraySet<>();
        private Session session;
    
        @OnOpen
        public void onOpen(Session session) {
            this.session = session;
            connections.add(this);
            System.out.println("New connection opened: " + session.getId());
        }
    
        @OnMessage
        public void onMessage(String message, Session session) {
            System.out.println("Message received: " + message);
            broadcast(message);
        }
    
        @OnClose
        public void onClose(Session session) {
            connections.remove(this);
            System.out.println("Connection closed: " + session.getId());
        }
    
        @OnError
        public void onError(Session session, Throwable throwable) {
            System.err.println("Error occurred: " + throwable.getMessage());
        }
    
        private void broadcast(String message) {
            for (ChatServer client : connections) {
                try {
                    client.session.getBasicRemote().sendText(message);
                } catch (IOException e) {
                    System.err.println("Broadcast error: " + e.getMessage());
                }
            }
        }
    }
    
    WebSocket Client
    
    import javax.websocket.*;
    import java.net.URI;
    import java.util.Scanner;
    
    @ClientEndpoint
    public class ChatClient {
    
        private Session session;
    
        public ChatClient(URI endpointURI) {
            try {
                WebSocketContainer container = ContainerProvider.getWebSocketContainer();
                container.connectToServer(this, endpointURI);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    
        @OnOpen
        public void onOpen(Session session) {
            this.session = session;
            System.out.println("Connected to server");
        }
    
        @OnMessage
        public void onMessage(String message) {
            System.out.println("Received: " + message);
        }
    
        @OnClose
        public void onClose(Session session) {
            System.out.println("Connection closed");
        }
    
        @OnError
        public void onError(Session session, Throwable throwable) {
            System.err.println("Error: " + throwable.getMessage());
        }
    
        public void sendMessage(String message) {
            try {
                session.getBasicRemote().sendText(message);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    
        public static void main(String[] args) {
            try {
                URI uri = new URI("ws://localhost:8080/chat");
                ChatClient client = new ChatClient(uri);
    
                Scanner scanner = new Scanner(System.in);
                while (true) {
                    System.out.print("Enter message: ");
                    String message = scanner.nextLine();
                    client.sendMessage(message);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    
}