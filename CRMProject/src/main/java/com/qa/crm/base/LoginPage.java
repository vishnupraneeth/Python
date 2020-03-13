package com.qa.crm.base;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage extends TestBase{
 //Actions to be performed on Login
 //1) Locate and enter username
 //2) Locate and enter password
 //3) click on login button 
//4) click on signup link 		

  @FindBy(name="username")
  WebElement usrname;
  
  @FindBy(name="password")
  WebElement password;
  
  @FindBy(xpath="//input[@value='Login' and @type='submit'] ")
  WebElement Loginbtn;
  
  @FindBy(xpath=" //a[contains(text(),'Sign Up']  " )
  WebElement signupbtn;
  
  public LoginPage(){
	  
	  PageFactory.initElements(driver, this);
	  
  }
  
  
  public void performaction(String usname,String pwd) {
	  usrname.sendKeys(usname);
	  password.sendKeys(pwd);
	  Loginbtn.click();
	  
  }
  
  public void perfomsignupaction() {
	  signupbtn.click();
	  
  }
  



}
