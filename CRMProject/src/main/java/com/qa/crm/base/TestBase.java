package com.qa.crm.base;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestBase {


	// 1) configure the driver and open the chrome 
	// 2) enter the url
	public static Properties p ;
	public static WebDriver driver;
	public TestBase(){
	
	
	try {
		FileInputStream fis=new FileInputStream("C:\\Users\\V-MUPRAN\\eclipse-workspace\\CRMProject\\src\\main\\java\\com\\qa\\crm\\config\\config.properties");
		p=new Properties();
		p.load(fis);
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
	}
	public void initiliazition() {
		
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\V-MUPRAN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe");
		driver=new ChromeDriver();
		
		if(p.getProperty("browser").equalsIgnoreCase("chrome"))
		{
			driver=new ChromeDriver();	
	    }
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		driver.manage().timeouts().pageLoadTimeout(1000, TimeUnit.SECONDS);
		p.getProperty("url");
		
	
	
	}

}
