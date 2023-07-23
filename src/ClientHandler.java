import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

class ClientHandler implements Runnable {
    private Socket clientSocket;
    private GameServer server;
    private BufferedReader in;

    public ClientHandler(Socket socket, GameServer server) throws IOException {
        this.clientSocket = socket;
        this.server = server;
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    @Override
    public void run() {
        String receivedMessage;
        while (true) {
            try {
                if (!((receivedMessage = in.readLine()) != null))
                    // This is where the board takes a message and starts writing it in the board.
                    // Mutex lock function called here
                    // Board also gives conformation if the block is currently busy or not.
                    break;
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            // Broadcast received message to all clients
            server.broadcast(receivedMessage);
        }
    }
}