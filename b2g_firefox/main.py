import os;
import sys;
import time;
import random;

# B2G boot log keys patched

def firefox_boot():

    boot_os   =   [];
    c = boot_os.append("start gai loader");
    return c;


def firefox_patch():
	#this only patch firefox boot
	c = firefox_boot();
	boot_key = ["omem_key", 
				"web_keyBoot",
				"app_web_boot",
				"API", {"value":0}, 
						{"reloadBootKeys":0}, 
						{"bindings_patch":"system_set"}];

	return boot_key;


def firefox_time():
	ctime = time.time();
	return ctime;




startKey = firefox_patch();
if({"bindings_patch"}):
	keysOmem = [];
	keysOmem.append("Booting to B2G Firefox.....");
	keysOmem;
	print("---------Firefox B2g Loader v1-----------------");
	print(keysOmem[0]);

	pkfile = os.mkdir("boot");

	# getting elapsed time
	cytime = time.time();
	print("Time Elapased Ran :", cytime);
	# getting random boot
	cfrand = random.randint(100000000000,700000000000);
	print("Time Booted : ", cfrand);
	print ("-----------------------------------------------");