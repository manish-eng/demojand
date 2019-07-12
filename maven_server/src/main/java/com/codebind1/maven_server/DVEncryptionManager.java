package com.codebind1.maven_server;
import java.io.UnsupportedEncodingException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import org.apache.commons.codec.binary.Base64;


public class DVEncryptionManager
{
   
   private static final String ENCRYPTION_IV = "cab193ea9542ffab";
   

   public String encode(String secretkey, String plainText) throws NullPointerException 
   {
      
      if (secretkey.length() == 0 || secretkey == null) {
          throw new NullPointerException("Please give Password");
      }
     
      if (plainText.length() == 0 || plainText == null) {
          throw new NullPointerException("Please give text");
      }
     
      try {
          SecretKeySpec skeySpec = getKey(secretkey);
//          byte[] clearText = stringToEncode.getBytes("UTF8");
         
          // IMPORTANT TO GET SAME RESULTS ON iOS and ANDROID

          IvParameterSpec ivParameterSpec = new IvParameterSpec(ENCRYPTION_IV.getBytes("UTF-8"));
         
          // Cipher is not thread safe
          Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
          cipher.init(Cipher.ENCRYPT_MODE, skeySpec, ivParameterSpec);
         
         
          String encrypedValue=Base64.encodeBase64String(cipher.doFinal(plainText.getBytes("UTF-8")));
         
 
          encrypedValue = encrypedValue.replaceAll("\\n", "");
          encrypedValue = encrypedValue.replaceAll("\\r", "");
         
         
         
 
          return encrypedValue;
         
      } catch (InvalidKeyException e) {
          e.printStackTrace();
      } catch (UnsupportedEncodingException e) {
          e.printStackTrace();
      } catch (NoSuchAlgorithmException e) {
          e.printStackTrace();
      } catch (BadPaddingException e) {
          e.printStackTrace();
      } catch (NoSuchPaddingException e) {
          e.printStackTrace();
      } catch (IllegalBlockSizeException e) {
          e.printStackTrace();
      } catch (InvalidAlgorithmParameterException e) {
          e.printStackTrace();
      }
      return "";
   }

   /**
   * Decodes a String using AES-256 and Base64
   *
   * @param context
   * @param secretKey
   * @param cipherText
   * @return desoded String
   */
   public String decode(String secretKey, String cipherText) throws NullPointerException 
   {
 
      if (secretKey.length() == 0 || secretKey == null) {
          throw new NullPointerException("Please give Password");
      }
     
      if (cipherText == null || cipherText.length() == 0) {
          throw new NullPointerException("Please give text");
      }
      cipherText = cipherText.replaceAll("\\n", "");
      cipherText = cipherText.replaceAll("\\r", "");
     
      try {
          SecretKey key = getKey(secretKey);
         
          // IMPORTANT TO GET SAME RESULTS ON iOS and ANDROID
      
          IvParameterSpec ivParameterSpec = new IvParameterSpec(ENCRYPTION_IV.getBytes("UTF-8"));
         
          byte[] encrypedPwdBytes = Base64.decodeBase64(cipherText);
          // cipher is not thread safe
          Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
          byte[] iv = new byte[cipher.getBlockSize()];

          IvParameterSpec ivParams = new IvParameterSpec(iv);
          cipher.init(Cipher.DECRYPT_MODE, key,ivParameterSpec);
//          cipher.init(Cipher.DECRYPT_MODE, key);
         
          byte[] decrypedValueBytes = (cipher.doFinal(encrypedPwdBytes));
         
          String decrypedValue = new String(decrypedValueBytes);
 
          return decrypedValue;
         
      } catch (InvalidKeyException e) {
          e.printStackTrace();
      } catch (UnsupportedEncodingException e) {
          e.printStackTrace();
      } catch (NoSuchAlgorithmException e) {
          e.printStackTrace();
      } catch (BadPaddingException e) {
          e.printStackTrace();
      } catch (NoSuchPaddingException e) {
          e.printStackTrace();
      } catch (IllegalBlockSizeException e) {
          e.printStackTrace();
      } catch (Exception e) {
          e.printStackTrace();
      }
      return "";
   }
   /**
   * Generates a SecretKeySpec for given password
   *
   * @param password
   * @return SecretKeySpec
   * @throws UnsupportedEncodingException
   */
   private static SecretKeySpec getKey(String password) throws UnsupportedEncodingException {
     
      // You can change it to 128 if you wish
      int keyLength = 256;
      byte[] keyBytes = new byte[keyLength / 8];
      // explicitly fill with zeros
      Arrays.fill(keyBytes, (byte) 0x0);
     
      // if password is shorter then key length, it will be zero-padded
      // to key length
      byte[] passwordBytes = password.getBytes("UTF-8");
      int length = passwordBytes.length < keyBytes.length ? passwordBytes.length : keyBytes.length;
      System.arraycopy(passwordBytes, 0, keyBytes, 0, length);
      SecretKeySpec key = new SecretKeySpec(keyBytes, "AES");
      return key;
   }
  
}