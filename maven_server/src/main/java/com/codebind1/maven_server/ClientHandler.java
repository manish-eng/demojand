package com.codebind1.maven_server;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.Random;

public class ClientHandler extends Thread {
	final BufferedReader din;
	final BufferedWriter dout;
	final Socket s;

	public ClientHandler(BufferedReader din, BufferedWriter dout, Socket s) {
		super();
		this.din = din;
		this.dout = dout;
		this.s = s;
	}
 

	private String getSaltString() {
		String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		StringBuilder salt = new StringBuilder();
		Random rnd = new Random();
		while (salt.length() < 32) { // length of the random string.
			int index = (int) (rnd.nextFloat() * SALTCHARS.length());
			salt.append(SALTCHARS.charAt(index));
		}
		String saltStr = salt.toString();
		return saltStr;

	}

	public void run() {
		String default_key = "krapesidarapnnywkeepdnoceroom710";
		DVEncryptionManager encryptDecript = new DVEncryptionManager();
		BufferedWriter dout = null;
			try{
				InputStream inputStream = s.getInputStream();
				dout = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
			}catch(Exception e) {
				
			}
			 
		 
		Server ob = new Server(din, dout,s);
		System.out.println("server started ");
//		try {
//			start = exchangeProcess(ob2, default_key);
//		} catch (IOException e1) {
//
//			e1.printStackTrace();
//		}
//		
//		if (start == true) {

		while (true) {

			try {
				String input_string = din.readLine();
				//System.out.println(input_string);
				String decoded_input_string = encryptDecript.decode(default_key, input_string);
				System.out.println(decoded_input_string); // decoding to get key_exchange

				if (decoded_input_string.equalsIgnoreCase("key_exchange")) {
				 System.out.println("REC Key exchange ");
					String new_key = getSaltString().toLowerCase();
					String handshake = encryptDecript.encode(default_key, "key_exchange");
					dout.write(handshake+"_"+default_key+"\r\n");
					// default_key = new_key;
					dout.flush();
				
				}
				else if (decoded_input_string.contains("key_")) {
					 System.out.println("REC Key  ");
						String new_key = decoded_input_string.substring(4);
						System.out.println("New key : "+new_key);
						default_key=new_key;
					
					}
				
				
//				if(decoded_input_string.equalsIgnoreCase("m01_c01_10042a5")) 
//				{
//					dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
//					dout.flush();
//				}
//				else if(decoded_input_string.equalsIgnoreCase("m01_c01_00082f4")) 
//				{
//					dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
//					dout.flush();
//				}
//				

				String module_id = decoded_input_string.substring(1, 3);
				if (module_id.contentEquals("01")) {
					ob.light_update(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("02")) {
					ob.drape_control(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("03")) {
					ob.ac_control(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("04")) {
					ob.door_control(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("05")) {
					ob.door_bell(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("06")) {
					ob.dnd_control(default_key, decoded_input_string, encryptDecript);
				} else if (module_id.contentEquals("07")) {
					ob.mmr_control(default_key, decoded_input_string, encryptDecript);
				} else {
					System.out.println("Connected");
				}
Thread.sleep(10);
			} catch (Exception e) {
				e.printStackTrace();
				System.out.println("connection closed");
				break;
			}
		}
	}
}
