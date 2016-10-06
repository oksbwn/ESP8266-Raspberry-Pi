public class Exec {
  public static void main(String args[]) {
    try {
      String line;
      Process p = Runtime.getRuntime().exec("cmd /c dir");
      BufferedReader bri = new BufferedReader
        (new InputStreamReader(p.getInputStream()));
     
      while ((line = bri.readLine()) != null) {
        System.out.println(line);
      }
      bri.close();
      bre.close();
      p.waitFor();
      System.out.println("Done.");
    }
    catch (Exception err) {
      err.printStackTrace();
    }
  }
}