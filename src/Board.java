public class Board {
    private static final int SIZE = 8;
    private int[][] boxes;
    private boolean[][] inProgress;

    public Board() {
        boxes = new int[SIZE][SIZE];
        inProgress = new boolean[SIZE][SIZE];
    }
}
