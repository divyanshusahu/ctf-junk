import java.applet.Applet;
import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Color;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;
import java.net.URLConnection;






public class Training
  extends Applet
  implements ActionListener
{
  Label mylabel;
  Label answer;
  TextField code;
  Button mybutton;
  
  public void init()
  {
    add(mylabel);
    add(code);
    add(mybutton);
    add(answer);
    
    mybutton.addActionListener(this);
    
    mylabel.setBackground(Color.black);
    mylabel.setForeground(Color.green);
    
    answer.setBackground(Color.black);
    answer.setForeground(Color.yellow);
    
    code.setForeground(Color.black);
    
    setBackground(Color.black);
    
    setLayout(new BorderLayout());
    add(mylabel, "West");
    add(code, "Center");
    add(mybutton, "East");
    add(answer, "South");
  }
  


  public void actionPerformed(ActionEvent paramActionEvent)
  {
    String str1 = code.getText();
    

    try
    {
      URL localURL = new URL("http://www.mod-x.co.uk/mod_x_LeV_2/M_LeVeL3_od/njk32rtraining.php");
      URLConnection localURLConnection = localURL.openConnection();
      String str2 = localURLConnection.getHeaderField("Training-code");
      

      if (str1.equals(str2))
      {

        String str3 = Base64.encodeString(str2);
        code.setText(str3 + ".php");
        answer.setText("Go to: " + str3 + ".php");

      }
      else
      {
        answer.setText("Incorrect");
      }
      
    }
    catch (Exception localException)
    {
      showStatus("An error occured, please report this to the Mod-X admins");
    }
  }
  

  public Training()
  {
    mylabel = new Label("Code: ");
    answer = new Label("", 1);
    code = new TextField(10);
    mybutton = new Button("Proceed...");
  }
}
