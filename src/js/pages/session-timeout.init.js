/*
  Name: Morvin -  Admin & Dashboard  
Author: Themesdesign
Contact: andzukor@gmail.com
File: Session Timeout
*/


$.sessionTimeout({
	keepAliveUrl: '/extras/pages/blank_page',
	logoutButton:'Logout',
	logoutUrl: '/extras/authentications/login',
	redirUrl: '/extras/authentications/lock_screen',
	warnAfter: 3000,
	redirAfter: 30000,
	countdownMessage: 'Redirecting in {timer} seconds.'
});