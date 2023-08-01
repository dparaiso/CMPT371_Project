import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

class GameServer {
    private final ServerSocket serverSocket;
    private static List<PrintWriter> clientWriters;

    public static Board gameBoard;


    public GameServer(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        clientWriters = new ArrayList<>();
        // Need to create and fit the board here
    }

    public void start() throws IOException {
        gameBoard = new Board(8);
        while (clientWriters.size() < 4) { // Accept up to 4 clients
            Socket clientSocket = serverSocket.accept();
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            clientWriters.add(out);
            new Thread(new ClientHandler(clientSocket, this)).start();

            String welcomeMessage = PlayerHandler.newPlayer(); // Give each client their own color
            out.println(welcomeMessage);
        }
    }

    // Method to broadcast a message to all clients
    public static void broadcast(String message) {
        for (PrintWriter writer : clientWriters) {
            writer.println(message);
        }
    }

    public static void main(String[] args) throws IOException {
        GameServer server = new GameServer(5000);
        server.start();
    }
}