Title: java 生成图片（仪表盘）
Date: 2010-06-29 16:56
Author: lmatt wang
Slug: java-shengchengtupianyibiaopan

[codesyntax lang="java"]

    package ict.dashboard;

    import java.awt.*;
    import java.awt.image.*;
    import java.io.*;
    import javax.imageio.*;
    import java.awt.font.FontRenderContext;
    import java.awt.geom.Rectangle2D;

    public class Dashboard{

        public static void generateImage(OutputStream os, double percent, int radius){

            //
            try{
                BufferedImage canvas = new BufferedImage(radius + radius, radius + radius, BufferedImage.TYPE_4BYTE_ABGR);
                Graphics2D g = (Graphics2D)canvas.createGraphics();//Graphics2D用于画图
                BufferedImage bg = ImageIO.read(new File("./image/bg.png"));//仪表盘背景
                BufferedImage pointer = ImageIO.read(new File("./image/pointer.png"));//仪表盘指针

                int pw = pointer.getWidth();
                int ph = pointer.getHeight();

                g.drawImage(bg, 0, 0, radius + radius, radius + radius, null);

                if(percent > 1.0) percent = 1.0;
                else if(percent < 0.0) percent = 0.0;
                double arc = Math.PI / 6.0 + percent * 300 / 360 * Math.PI * 2;

                g.rotate(arc, radius, radius);//旋转
                g.drawImage(pointer, radius - pw / 2, radius - 40, 20, radius, null);

                g.rotate(-arc, radius, radius);
                String ps = String.valueOf(percent);
                if(ps.length() > 5) ps = ps.substring(0, 5);//截断字符串
                FontRenderContext context = g.getFontRenderContext();
                Font font = new Font("Serif", Font.BOLD, 20);
                Rectangle2D bounds = font.getStringBounds(ps, context);//获取字符串边界信息，如长、宽等
                g.setColor(Color.WHITE);
                g.fillRect((int)(radius - bounds.getWidth() / 2) - 1, (int)(radius - bounds.getHeight() / 2) - 1, (int)bounds.getWidth() + 1, (int)bounds.getHeight() + 1);
                g.setColor(Color.BLACK);
                g.setFont(font);//字体设置
                g.drawString(ps, (int)(radius - bounds.getWidth() / 2), (int)(radius - bounds.getHeight() / 2 - bounds.getY()));//显示比率

                ImageIO.write(canvas, "png", os);//生成图片到outputstream
            }
            catch(Exception ex){

                System.out.println("generate image error!");
                System.out.println(ex);
            }
        }

        public static void main(String[] args) throws Exception{

    //-10.0到370度的测试
            for(double i = -10.0; i < 370.1; i += 10.0){

                FileOutputStream fos = new FileOutputStream(new File("./" + i + ".png"));
                generateImage(fos, i / 360.0, 200);
                fos.close();
            }
        }
    }

[/codesyntax]
