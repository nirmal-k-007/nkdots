import java.util.concurrent.CopyOnWriteArraySet;

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
    
       
}