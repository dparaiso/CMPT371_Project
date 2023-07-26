import java.util.ArrayList;

public class PlayerHandler {
    private static final String[] playerColor = {"blue", "red", "pink", "green"};
    private static int playerCount = 0;

    public static synchronized String newPlayer() {
        return playerColor[playerCount++ % playerColor.length];
    }
}
