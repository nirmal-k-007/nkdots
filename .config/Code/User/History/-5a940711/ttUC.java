import javax.sound.sampled.*;
import java.io.ByteArrayOutputStream;

public class AudioRecorder {
    public static void main(String[] args) {
        // Audio format settings
        AudioFormat format = new AudioFormat(44100, 16, 1, true, true); // 44.1kHz, 16-bit, mono, signed, big-endian
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        if (!AudioSystem.isLineSupported(info)) {
            System.out.println("Microphone not supported!");
            return;
        }

        try (TargetDataLine microphone = (TargetDataLine) AudioSystem.getLine(info);
             ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {

            // Open and start the microphone
            microphone.open(format);
            microphone.start();
            System.out.println("Recording audio... Press Ctrl+C to stop.");

            byte[] buffer = new byte[1024]; // Buffer for microphone data
            int bytesRead;

            // Read audio data and save it to byte array
            while (true) {
                bytesRead = microphone.read(buffer, 0, buffer.length);
                byteArrayOutputStream.write(buffer, 0, bytesRead);

                // Optional: break after a specific duration
                // For example, stop after 10 seconds:
                // if (byteArrayOutputStream.size() > format.getFrameSize() * format.getFrameRate() * 10) break;
            }

            // Convert to byte array
            byte[] audioBytes = byteArrayOutputStream.toByteArray();
            System.out.println("Recording complete. Captured " + audioBytes.length + " bytes of audio.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
