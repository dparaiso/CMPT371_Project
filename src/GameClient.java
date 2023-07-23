import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class GameClient {
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public GameClient(String serverAddress, int serverPort) throws IOException {
        clientSocket = new Socket(serverAddress, serverPort);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    public void send(String message) {
        out.println(message);
    }

    public void start() throws IOException {
        Thread listenThread = new Thread(() -> {
            String serverMessage;
            try {
                while ((serverMessage = in.readLine()) != null) {
                    System.out.println("Received: " + serverMessage);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        listenThread.start();

        BufferedReader userInputReader = new BufferedReader(new InputStreamReader(System.in));
        String userInput;
        while ((userInput = userInputReader.readLine()) != null) {
            send(userInput);
        }
    }

    public static void main(String[] args) throws IOException {
        GameClient client = new GameClient("localhost", 5000);
        client.start();
    }
}
