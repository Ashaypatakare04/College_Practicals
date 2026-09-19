import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class FactorialApplet extends Applet implements ActionListener {
    Label l1, l2;
    TextField t1, t2;
    Button b1;

    public void init() {
        l1 = new Label("Enter Number:");
        t1 = new TextField(10);
        b1 = new Button("Calculate");
        l2 = new Label("Factorial:");
        t2 = new TextField(10);
        t2.setEditable(false);
        add(l1); add(t1); add(b1); add(l2); add(t2);
        b1.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            int n = Integer.parseInt(t1.getText());
            long fact = 1;
            for (int i = 1; i <= n; i++) fact *= i;
            t2.setText(String.valueOf(fact));
        } catch (Exception ex) { t2.setText("Error"); }
    }
}
