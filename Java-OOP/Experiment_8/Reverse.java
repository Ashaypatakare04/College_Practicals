import javax.swing.*;
public class Reverse{
public static void main(String[] args){
JFrame f=new JFrame("Reverse Number");
JTextField t=new JTextField(10);
JButton b=new JButton("Reverse");
JLabel l=new JLabel();

f.setSize(300,150);
f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
f.setLayout(new java.awt.FlowLayout());

b.addActionListener(e->{
String num=t.getText();
String r=new StringBuilder(num).reverse().toString();
l.setText("Reverse:"+r);
});

f.add(t);
f.add(b);
f.add(l);

f.setVisible(true);

}
}
