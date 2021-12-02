describe('Login Page for Smartbear Software',()=> {
	it('Protractor Login', () => { 
		browser.waitForAngularEnabled(false); 
			browser.get('http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx') 
			.then(() => element(by.id('ctl00_MainContent_username')).sendKeys('Tester'))  // then keyword is used to chain
			.then(() => element(by.id('ctl00_MainContent_password')).sendKeys('test')) 
            .then(() => element(by.name('ctl00$MainContent$login_button')).click())
			browser.getCurrentUrl().then((url) => {
				expect(url).toBe('http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/default.aspx');})
		});
    it('Protractor view all products', () => {
		browser.waitForAngularEnabled(false);
		element(by.linkText ('View all products')).click();		
        //then(() => {var String ,Sample = driver.getTitle()})
        //then(() => System.out.println("Sample"))
			
    });
	});