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
                    break;
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            receivedMessage = receivedMessage.replaceAll("\\s", "");
            String[] clientcommand = receivedMessage.split("\\,");
//            }
            if(clientcommand[0].equals("server")){
                if (clientcommand[1].equals("fill")){
                    if (!GameServer.gameBoard.startFillingBox(Integer.parseInt(clientcommand[3]), Integer.parseInt(clientcommand[4]), clientcommand[2])){
                        GameServer.gameBoard.failedFillingBox(Integer.parseInt(clientcommand[3]), Integer.parseInt(clientcommand[4]), clientcommand[2]);
                    }
                }
                if(clientcommand[1].equals("success")){
                    GameServer.gameBoard.successfulFillingBox(Integer.parseInt(clientcommand[3]), Integer.parseInt(clientcommand[4]), clientcommand[2]);
                }
                if(clientcommand[1].equals("failed")){
                    GameServer.gameBoard.failedFillingBox(Integer.parseInt(clientcommand[3]), Integer.parseInt(clientcommand[4]), clientcommand[2]);
                }
            }
            System.out.println(receivedMessage);

            //Received: server, fill, blue, 1, 3
            //The line below maybe redundat
            //server.broadcast(receivedMessage);
        }
    }
}