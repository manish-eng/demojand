package com.codebind1.maven_server;

import java.net.*;

import java.io.*;

public class Server {
	final BufferedReader din;
	final BufferedWriter dout;
	final Socket s;

public Server(BufferedReader din, BufferedWriter dout, Socket s) {
		super();
		this.din = din;
		this.dout = dout;
		this.s = s;
	}
	public void light_update(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException { // 01
		 
		if (decoded_input_string.substring(5, 7).contentEquals("01")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}
		} else if (decoded_input_string.substring(5, 7).contentEquals("02")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}  
		} else if (decoded_input_string.substring(5, 7).contentEquals("03")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}
		} else if (decoded_input_string.substring(5, 7).contentEquals("04")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}
		} else if (decoded_input_string.substring(5, 7).contentEquals("05")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}
		} else if (decoded_input_string.substring(5, 7).contentEquals("06")) {
			if (decoded_input_string.substring(8, 11).contentEquals("100")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}    
	}
}


	public void light_status(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException {
		if (decoded_input_string.substring(4, 11).contentEquals("c??_???")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		} else if (decoded_input_string.substring(8, 11).contentEquals("???")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		} else
			System.out.println("sorry wrong input");
	}

	public void drape_control(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException { // 02
		if (decoded_input_string.substring(5, 7).contentEquals("01")) {
			if (decoded_input_string.substring(8, 11).contentEquals("001")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("002")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} 
		} else if(decoded_input_string.substring(5, 7).contentEquals("02")){
			if (decoded_input_string.substring(8, 11).contentEquals("001")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("002")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} 
		}
		
	}

	public void ac_control(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException { // 03
		if (decoded_input_string.substring(5, 7).contentEquals("01")) {
			if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("001")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("002")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("003")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("004")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
				dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
				dout.flush();
			}  
		}  
	}

	public void door_control(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException { // 04
		if (decoded_input_string.substring(8, 11).contentEquals("000")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		} else if (decoded_input_string.substring(8, 11).contentEquals("100")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		}  
	}
	
	public void door_bell(String key, String decoded_input_string, DVEncryptionManager ob) throws IOException { // 05
		if (decoded_input_string.substring(8, 11).contentEquals("100")) {
			String msg1 = "m05_c01_100";
			msg1 = ob.encode(key, msg1);
			dout.write(msg1);
		} else {
			String msg1 = "wrong input";
			dout.write(msg1);
		}

	}

	public void dnd_control(String default_key, String decoded_input_string, DVEncryptionManager encryptDecript) throws IOException { // 06
		if (decoded_input_string.substring(8, 11).contentEquals("100")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
			dout.write(encryptDecript.encode(default_key,decoded_input_string)+"\r\n");
			dout.flush();
		} 
	}

	public void mmr_control(String key, String decoded_input_string, DVEncryptionManager ob) throws IOException { // 07
		if (decoded_input_string.substring(8, 11).contentEquals("100")) {
			String msg1 = "m07_c01_100";
			msg1 = ob.encode(key, msg1);
			dout.write(msg1);
		} else if (decoded_input_string.substring(8, 11).contentEquals("000")) {
			String msg1 = "m07_c01_000";
			msg1 = ob.encode(key, msg1);
			dout.write(msg1);
		} else {
			String msg1 = "wrong input";
			dout.write(msg1);
		}

	}

	public static void main(String args[]) throws Exception {

		System.out.println("Server Started!");
		ServerSocket ss = new ServerSocket(5000);

		while (true) {

			try {
				Socket s = ss.accept();
				InputStream inputStream = s.getInputStream();
				BufferedReader din = new BufferedReader(new InputStreamReader(inputStream));
				BufferedWriter dout = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
				Thread t = new ClientHandler(din, dout, s);
				t.start();
				Server obj = new Server(din, dout, s);
			} catch (Exception e) {
				ss.close();
				break;
			}
		}
	}

}
