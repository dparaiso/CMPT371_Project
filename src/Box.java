import java.util.Objects;

class Box {
    private String color = "white";
    private boolean isLocked = false;

    public String getColor() {
        return color;
    }

    public boolean isLocked() {
        return isLocked;
    }
    public synchronized boolean startFill(String color){
        if(isLocked || !Objects.equals(color, "white")){
            return false;
        }
        else{
            isLocked = true;
            // Change color of box to indicate the box is being filled
            return true;
        }
    }

    public synchronized boolean successfulFill(String color){
        this.color = color;
        return true;
    }

    public synchronized boolean failedFill (String color){
        this.color = "white";
        this.isLocked = false;
        return true;
    }
}