import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculatorGUI {
    private JTextField display;
    private double val1 = 0;
    private String op = "";
    private boolean start = true;

    public CalculatorGUI() {
        JFrame f = new JFrame("Calculator");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        display = new JTextField();
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);
        f.add(display, BorderLayout.NORTH);

        JPanel p = new JPanel(new GridLayout(6, 4, 5, 5));
        String[] btns = {
            "C", "%", "sq", "sqrt", "7", "8", "9", "/",
            "4", "5", "6", "*", "1", "2", "3", "-",
            "0", ".", "=", "+", "cube", "1/x", "+/-", "del"
        };
        for (String b : btns) {
            JButton btn = new JButton(b);
            btn.addActionListener(new Click());
            p.add(btn);
        }
        f.add(p);
        f.setSize(350, 450);
        f.setVisible(true);
    }

    private class Click implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            String c = e.getActionCommand();
            if (c.matches("[0-9\\.]")) {
                if (start) { display.setText(c); start = false; }
                else display.setText(display.getText() + c);
            } else if (c.equals("C")) { display.setText(""); val1 = 0; op = ""; }
            else if (c.equals("=")) { calc(); op = ""; }
            else if (c.equals("sq")) { double v = Double.parseDouble(display.getText()); display.setText(String.valueOf(v*v)); }
            else if (c.equals("sqrt")) { double v = Double.parseDouble(display.getText()); display.setText(String.valueOf(Math.sqrt(v))); }
            else if (c.equals("cube")) { double v = Double.parseDouble(display.getText()); display.setText(String.valueOf(v*v*v)); }
            else {
                if (!op.isEmpty()) calc();
                val1 = Double.parseDouble(display.getText());
                op = c;
                start = true;
            }
        }
        private void calc() {
            double v2 = Double.parseDouble(display.getText());
            switch(op) {
                case "+": val1 += v2; break;
                case "-": val1 -= v2; break;
                case "*": val1 *= v2; break;
                case "/": val1 /= v2; break;
                case "%": val1 %= v2; break;
            }
            display.setText(String.valueOf(val1));
            start = true;
        }
    }
    public static void main(String[] args) { new CalculatorGUI(); }
}
