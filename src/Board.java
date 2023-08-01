import java.util.*;

public class Board {
    private static Box[][] boxes;

    public static class PlayerScore {
        public String color;
        public int score;

        public PlayerScore(String color, int score) {
            this.color = color;
            this.score = score;
        }

        public int getScore(){
            return this.score;
        }

        @Override
        public String toString() {
            return color + ": " + score;
        }
    }

    public Board(int size) {
        boxes = new Box[size][size];
        for (Box[] row : boxes) {
            Arrays.fill(row, new Box());
        }
    }

    public Box getBox(int x, int y){
        return boxes[x][y];
    }

    public static boolean startFillingBox(int x, int y, String color){

        if( boxes[x][y].startFill(color)){
            String fillMessage = "[fill, "+color+ ", "+ Integer.toString(x)+ ", " + Integer.toString(y) + "]";
            GameServer.broadcast(fillMessage);
            return true;
        }else{
            return false;
        }
    }

    public static void failedFillingBox(int x, int y, String color){
        if (boxes[x][y].failedFill(color)) {
            String failMessage = "[fail, " + color + ", " + Integer.toString(x) + ", " + Integer.toString(y) + "]";
            GameServer.broadcast(failMessage);
        }
    }

    public static void successfulFillingBox(int x, int y, String color){
        boxes[x][y].successfulFill(color);
        String successMessage = "[success, " + color + ", " + Integer.toString(x) + ", " + Integer.toString(y) + "]";
        GameServer.broadcast(successMessage);
    }

    public ArrayList<String> findWinner(){
        int blue = 0;
        int red = 0;
        int pink = 0;
        int green = 0;
        for(int i = 0; i < 8; i++) {
            for(int j = 0; j < 8; j++){
                if(boxes[i][j].getColor().equals("blue")){
                    blue++;
                }
                if(boxes[i][j].getColor().equals("red")){
                    red++;
                }
                if(boxes[i][j].getColor().equals("pink")){
                    pink++;
                }
                if(boxes[i][j].getColor().equals("green")){
                    green++;
                }

            }
        }
        ArrayList<PlayerScore> scores = new ArrayList<>();
        scores.add(new PlayerScore("blue", blue));
        scores.add(new PlayerScore("red", red));
        scores.add(new PlayerScore("pink", pink));
        scores.add(new PlayerScore("green", green));

        scores.sort((PlayerScore a, PlayerScore b) -> b.getScore() - a.getScore());

        ArrayList<String> results = new ArrayList<>();
        for (PlayerScore ps : scores) {
            results.add(ps.toString());
        }

        return results;

    }
    // output format
    // ["green: 22", "red: 20", "pink: 18", "blue: 15"]

}
