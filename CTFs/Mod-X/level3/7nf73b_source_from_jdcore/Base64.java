import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FilterInputStream;
import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.Serializable;






















public class Base64
{
  public static final boolean ENCODE = true;
  public static final boolean DECODE = false;
  private static final int MAX_LINE_LENGTH = 76;
  private static final byte EQUALS_SIGN = 61;
  private static final byte NEW_LINE = 10;
  private static final byte[] ALPHABET = { 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47 };
  
















  private static final byte[] DECODABET = { -9, -9, -9, -9, -9, -9, -9, -9, -9, -5, -5, -9, -9, -5, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -5, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, 62, -9, -9, -9, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -9, -9, -9, -1, -9, -9, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -9, -9, -9, -9, -9, -9, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -9, -9, -9, -9 };
  







  private static final byte BAD_ENCODING = -9;
  







  private static final byte WHITE_SPACE_ENC = -5;
  







  private static final byte EQUALS_SIGN_ENC = -1;
  








  private Base64() {}
  







  public static void main(String[] paramArrayOfString)
  {
    String str = "Hello, world";
    str = "abcd";
    


    byte[] arrayOfByte1 = encodeString(str).getBytes();
    byte[] arrayOfByte2 = decode(arrayOfByte1, 0, arrayOfByte1.length);
    
    System.out.println("\n\n" + str + ":" + new String(arrayOfByte1) + ":" + new String(arrayOfByte2));
    
    try
    {
      FileInputStream localFileInputStream = new FileInputStream("c:\\abcd.txt");
      Base64.InputStream localInputStream = new Base64.InputStream(localFileInputStream, false);
      int i = 0;
      while ((i = localInputStream.read()) > 0) {}

    }
    catch (Exception localException)
    {
      localException.printStackTrace();
    }
  }
  











  private static byte[] encode3to4(byte[] paramArrayOfByte)
  {
    return encode3to4(paramArrayOfByte, 3);
  }
  














  private static byte[] encode3to4(byte[] paramArrayOfByte, int paramInt)
  {
    byte[] arrayOfByte = new byte[4];
    encode3to4(paramArrayOfByte, 0, paramInt, arrayOfByte, 0);
    return arrayOfByte;
  }
  




































  private static byte[] encode3to4(byte[] paramArrayOfByte1, int paramInt1, int paramInt2, byte[] paramArrayOfByte2, int paramInt3)
  {
    int i = (paramInt2 > 0 ? paramArrayOfByte1[paramInt1] << 24 >>> 8 : 0) | (paramInt2 > 1 ? paramArrayOfByte1[(paramInt1 + 1)] << 24 >>> 16 : 0) | (paramInt2 > 2 ? paramArrayOfByte1[(paramInt1 + 2)] << 24 >>> 24 : 0);
    


    switch (paramInt2)
    {
    case 3: 
      paramArrayOfByte2[paramInt3] = ALPHABET[(i >>> 18)];
      paramArrayOfByte2[(paramInt3 + 1)] = ALPHABET[(i >>> 12 & 0x3F)];
      paramArrayOfByte2[(paramInt3 + 2)] = ALPHABET[(i >>> 6 & 0x3F)];
      paramArrayOfByte2[(paramInt3 + 3)] = ALPHABET[(i & 0x3F)];
      return paramArrayOfByte2;
    
    case 2: 
      paramArrayOfByte2[paramInt3] = ALPHABET[(i >>> 18)];
      paramArrayOfByte2[(paramInt3 + 1)] = ALPHABET[(i >>> 12 & 0x3F)];
      paramArrayOfByte2[(paramInt3 + 2)] = ALPHABET[(i >>> 6 & 0x3F)];
      paramArrayOfByte2[(paramInt3 + 3)] = 61;
      return paramArrayOfByte2;
    
    case 1: 
      paramArrayOfByte2[paramInt3] = ALPHABET[(i >>> 18)];
      paramArrayOfByte2[(paramInt3 + 1)] = ALPHABET[(i >>> 12 & 0x3F)];
      paramArrayOfByte2[(paramInt3 + 2)] = 61;
      paramArrayOfByte2[(paramInt3 + 3)] = 61;
      return paramArrayOfByte2;
    }
    
    return paramArrayOfByte2;
  }
  












  public static String encodeObject(Serializable paramSerializable)
  {
    ByteArrayOutputStream localByteArrayOutputStream = null;
    Base64.OutputStream localOutputStream = null;
    ObjectOutputStream localObjectOutputStream = null;
    
    try
    {
      localByteArrayOutputStream = new ByteArrayOutputStream();
      localOutputStream = new Base64.OutputStream(localByteArrayOutputStream, true);
      localObjectOutputStream = new ObjectOutputStream(localOutputStream);
      
      localObjectOutputStream.writeObject(paramSerializable);
    }
    catch (IOException localIOException)
    {
      localIOException.printStackTrace();
      return null;
    }
    finally {
      try {
        localObjectOutputStream.close(); } catch (Exception localException1) {}
      try { localOutputStream.close(); } catch (Exception localException2) {}
      try { localByteArrayOutputStream.close();
      } catch (Exception localException3) {}
    }
    return new String(localByteArrayOutputStream.toByteArray());
  }
  








  public static String encodeBytes(byte[] paramArrayOfByte)
  {
    return encodeBytes(paramArrayOfByte, 0, paramArrayOfByte.length);
  }
  











  public static String encodeBytes(byte[] paramArrayOfByte, int paramInt1, int paramInt2)
  {
    int i = paramInt2 * 4 / 3;
    byte[] arrayOfByte = new byte[i + (paramInt2 % 3 > 0 ? 4 : 0) + i / 76];
    

    int j = 0;
    int k = 0;
    int m = paramInt2 - 2;
    int n = 0;
    for (; j < m; k += 4)
    {
      encode3to4(paramArrayOfByte, j, 3, arrayOfByte, k);
      
      n += 4;
      if (n == 76)
      {
        arrayOfByte[(k + 4)] = 10;
        k++;
        n = 0;
      }
      j += 3;
    }
    










    if (j < paramInt2)
    {
      encode3to4(paramArrayOfByte, j, paramInt2 - j, arrayOfByte, k);
      k += 4;
    }
    
    return new String(arrayOfByte, 0, k);
  }
  









  public static String encodeString(String paramString)
  {
    return encodeBytes(paramString.getBytes());
  }
  















  private static byte[] decode4to3(byte[] paramArrayOfByte)
  {
    byte[] arrayOfByte1 = new byte[3];
    int i = decode4to3(paramArrayOfByte, 0, arrayOfByte1, 0);
    byte[] arrayOfByte2 = new byte[i];
    
    for (int j = 0; j < i; j++) {
      arrayOfByte2[j] = arrayOfByte1[j];
    }
    return arrayOfByte2;
  }
  


























  private static int decode4to3(byte[] paramArrayOfByte1, int paramInt1, byte[] paramArrayOfByte2, int paramInt2)
  {
    if (paramArrayOfByte1[(paramInt1 + 2)] == 61)
    {
      i = DECODABET[paramArrayOfByte1[paramInt1]] << 24 >>> 6 | DECODABET[paramArrayOfByte1[(paramInt1 + 1)]] << 24 >>> 12;
      

      paramArrayOfByte2[paramInt2] = ((byte)(i >>> 16));
      return 1;
    }
    

    if (paramArrayOfByte1[(paramInt1 + 3)] == 61)
    {
      i = DECODABET[paramArrayOfByte1[paramInt1]] << 24 >>> 6 | DECODABET[paramArrayOfByte1[(paramInt1 + 1)]] << 24 >>> 12 | DECODABET[paramArrayOfByte1[(paramInt1 + 2)]] << 24 >>> 18;
      


      paramArrayOfByte2[paramInt2] = ((byte)(i >>> 16));
      paramArrayOfByte2[(paramInt2 + 1)] = ((byte)(i >>> 8));
      return 2;
    }
    



    int i = DECODABET[paramArrayOfByte1[paramInt1]] << 24 >>> 6 | DECODABET[paramArrayOfByte1[(paramInt1 + 1)]] << 24 >>> 12 | DECODABET[paramArrayOfByte1[(paramInt1 + 2)]] << 24 >>> 18 | DECODABET[paramArrayOfByte1[(paramInt1 + 3)]] << 24 >>> 24;
    



    paramArrayOfByte2[paramInt2] = ((byte)(i >> 16));
    paramArrayOfByte2[(paramInt2 + 1)] = ((byte)(i >> 8));
    paramArrayOfByte2[(paramInt2 + 2)] = ((byte)i);
    return 3;
  }
  










  public static byte[] decode(String paramString)
  {
    byte[] arrayOfByte = paramString.getBytes();
    return decode(arrayOfByte, 0, arrayOfByte.length);
  }
  










  public static String decodeToString(String paramString)
  {
    return new String(decode(paramString));
  }
  









  public static Object decodeToObject(String paramString)
  {
    byte[] arrayOfByte = decode(paramString);
    
    ByteArrayInputStream localByteArrayInputStream = null;
    ObjectInputStream localObjectInputStream = null;
    
    try
    {
      localByteArrayInputStream = new ByteArrayInputStream(arrayOfByte);
      localObjectInputStream = new ObjectInputStream(localByteArrayInputStream);
      
      return localObjectInputStream.readObject();
    }
    catch (IOException localIOException)
    {
      localIOException.printStackTrace();
      return null;
    }
    catch (ClassNotFoundException localClassNotFoundException) {
      Object localObject2;
      localClassNotFoundException.printStackTrace();
      return null;
    }
    finally {
      try {
        localByteArrayInputStream.close(); } catch (Exception localException7) {}
      try { localObjectInputStream.close();
      }
      catch (Exception localException8) {}
    }
  }
  









  public static byte[] decode(byte[] paramArrayOfByte, int paramInt1, int paramInt2)
  {
    int i = paramInt2 * 3 / 4;
    byte[] arrayOfByte1 = new byte[i];
    int j = 0;
    
    byte[] arrayOfByte2 = new byte[4];
    int k = 0;
    int m = 0;
    int n = 0;
    int i1 = 0;
    for (m = 0; m < paramInt2; m++)
    {
      n = (byte)(paramArrayOfByte[m] & 0x7F);
      i1 = DECODABET[n];
      
      if (i1 >= -5)
      {
        if (i1 >= -1)
        {
          arrayOfByte2[(k++)] = n;
          if (k > 3)
          {
            j += decode4to3(arrayOfByte2, 0, arrayOfByte1, j);
            k = 0;
            

            if (n == 61) {
              break;
            }
            
          }
        }
      }
      else
      {
        System.err.println("Bad Base64 input character at " + m + ": " + paramArrayOfByte[m] + "(decimal)");
        return null;
      }
    }
    
    byte[] arrayOfByte3 = new byte[j];
    System.arraycopy(arrayOfByte1, 0, arrayOfByte3, 0, j);
    return arrayOfByte3;
  }
  




  public static class InputStream
    extends FilterInputStream
  {
    private boolean encode;
    



    private int position;
    



    private byte[] buffer;
    


    private int bufferLength;
    


    private int numSigBytes;
    



    public InputStream(InputStream paramInputStream)
    {
      this(paramInputStream, false);
    }
    











    public InputStream(InputStream paramInputStream, boolean paramBoolean)
    {
      super();
      encode = paramBoolean;
      bufferLength = (paramBoolean ? 4 : 3);
      buffer = new byte[bufferLength];
      position = -1;
    }
    







    public int read()
      throws IOException
    {
      if (position < 0) { byte[] arrayOfByte;
        int j;
        if (encode)
        {
          arrayOfByte = new byte[3];
          numSigBytes = 0;
          for (j = 0; j < 3; j++)
          {
            try
            {
              int k = in.read();
              

              if (k >= 0)
              {
                arrayOfByte[j] = ((byte)k);
                numSigBytes += 1;
              }
              

            }
            catch (IOException localIOException)
            {
              if (j == 0) {
                throw localIOException;
              }
            }
          }
          
          if (numSigBytes > 0)
          {
            Base64.encode3to4(arrayOfByte, 0, numSigBytes, buffer, 0);
            position = 0;
          }
          

        }
        else
        {
          arrayOfByte = new byte[4];
          j = 0;
          for (j = 0; j < 4; j++)
          {
            int m = 0;
            do { m = in.read();
            } while ((m >= 0) && (Base64.DECODABET[(m & 0x7F)] < -5));
            
            if (m < 0) {
              break;
            }
            arrayOfByte[j] = ((byte)m);
          }
          
          if (j == 4)
          {
            numSigBytes = Base64.decode4to3(arrayOfByte, 0, buffer, 0);
            position = 0;
          }
        }
      }
      


      if (position >= 0)
      {

        if (position >= numSigBytes) {
          return -1;
        }
        int i = buffer[(position++)];
        
        if (position >= bufferLength) {
          position = -1;
        }
        return i;
      }
      


      return -1;
    }
    














    public int read(byte[] paramArrayOfByte, int paramInt1, int paramInt2)
      throws IOException
    {
      for (int i = 0; i < paramInt2; i++)
      {
        int j = read();
        
        if (j < 0) {
          return -1;
        }
        paramArrayOfByte[(paramInt1 + i)] = ((byte)j);
      }
      return i;
    }
  }
  




  public static class OutputStream
    extends FilterOutputStream
  {
    private boolean encode;
    



    private int position;
    



    private byte[] buffer;
    



    private int bufferLength;
    



    private int lineLength;
    




    public OutputStream(OutputStream paramOutputStream)
    {
      this(paramOutputStream, true);
    }
    












    public OutputStream(OutputStream paramOutputStream, boolean paramBoolean)
    {
      super();
      encode = paramBoolean;
      bufferLength = (paramBoolean ? 3 : 4);
      buffer = new byte[bufferLength];
      position = 0;
      lineLength = 0;
    }
    












    public void write(int paramInt)
      throws IOException
    {
      buffer[(position++)] = ((byte)paramInt);
      if (position >= bufferLength)
      {
        if (encode)
        {
          out.write(Base64.encode3to4(buffer, bufferLength));
          
          lineLength += 4;
          if (lineLength >= 76)
          {
            out.write(10);
            lineLength = 0;
          }
        }
        else {
          out.write(Base64.decode4to3(buffer));
        }
        position = 0;
      }
    }
    










    public void write(byte[] paramArrayOfByte, int paramInt1, int paramInt2)
      throws IOException
    {
      for (int i = 0; i < paramInt2; i++)
      {
        write(paramArrayOfByte[(paramInt1 + i)]);
      }
    }
    








    public void flush()
      throws IOException
    {
      if (position > 0)
      {
        if (encode)
        {
          out.write(Base64.encode3to4(buffer, position));
        }
        else
        {
          throw new IOException("Base64 input not properly padded.");
        }
      }
      
      super.flush();
      out.flush();
    }
    





    public void close()
      throws IOException
    {
      flush();
      
      super.close();
      out.close();
      
      buffer = null;
      out = null;
    }
  }
}
