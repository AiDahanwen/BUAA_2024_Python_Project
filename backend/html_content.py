html_content = """
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>[[PAGE_NAME]]</title>
	<meta name="generator" content="BBEdit 10.5" />
        <meta name="viewport" content="width=device-width" />
	
  <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+Gulf,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+HK,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+TC,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+KR,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+TH,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+JP,v1" type="text/css"/>
   <link rel="stylesheet" href="//www.apple.com/wss/fonts?families=SF+Pro,v1|SF+Pro+Icons,v1|SF+Pro+SC,v1" type="text/css"/>

<style>

  body#message {
  font-family: 'SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif !important;
  font-size: 17px;
  line-height: 25px;
  font-weight: normal;
  color: #333 !important;
  background-color: #ffffff !important;
  margin:0 !important; 
  padding:0 !important;
  width:100% /* !important */;
  /* was 685px */;
}

  /*
  same width as body, because Rover adds this div
  */

  body/*, .main*/ {
  }
  .main {
  width: 685px;
  }

  #apple-logo-left-margin {
  width: 538px !important;
  }
  #logo-row-box {
  width:100% !important;
  /* text-align:right; */
  padding-bottom:20px !important;
  }

   /* div[dir="rtl"] #logo-row-box {
           text-align:left !important;
       } */

h1 {
  font-size: 32px;
  line-height:36px;
  padding-bottom: 10px;
  border: 0 !important;
  color: 333 !important;
}

b {
  font-weight:500 !important;
  }

p {
  margin-top: 0 !important;
  word-wrap: break-word;
  color: #333;
}

  td.h1-header {
  padding:0px 0px 0px !important;
  }
  td.signature {
  padding-right:0 !important;
  padding-left:0 !important;
  }
  td.no-padding-bottom {
  padding-bottom:0 !important;
  }
  #signature {
  padding-top:18px !important; /* was 41px */
  padding-bottom:50px !important;
  }

  em a {
  color: #333 !important;
  }
  a {
  color: #0070c9;
  text-decoration: none;
  }
  span.unlink a,
  em a,
  b a,
  td.unlink a {
  color:#333 !important;
  cursor: text;
  pointer-events: none;
  padding-top:0 !important;
  margin-top:0 !important;
  }
  #main {
  margin-top: 40px;
  padding-right:15px;
  padding-left:15px;
  padding-bottom:30px;
  }

  footer,
  footer p,
  footer span.unlink a,
  footer td.paragraph {
  font-size:12px;
  line-height:18px;
  font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  color:#888 !important;
  }
  .center-text,
  footer nav,

  footer a:hover {
  text-decoration: underline;
  }
a:hover, a:focus {
  text-decoration: underline !important;
  }
  .no-margin-bottom {
  margin-bottom: 0 !important;
  }
  td.spacer-36 {
  padding-bottom:36px;
  }
  html[dir=rtl] #apple-logo {
  left:0;
  right:538px;
  }
  p#copyright {
  margin-bottom: 0;
  }
  .display-block {
  display: block;
  }
  .nowrap {
  white-space: nowrap;
  }
  #apple-logo-margin-bottom {
  height: 44px !important;
  }
  #left-align-on-reply {
  /* moved from body */
  margin:0px auto 50px;
  padding:0;
  width: 685px;
  }
  #apple-logo-cell {
  width:100%;
  padding-top:40px;
  padding-bottom:44px;
  }
  #apple-logo-in-cell {
  height: 28px !important;
  width: 24px !important;
  }
  #apple-logo-in-row-box-mobile {
  display: none;
  height: 20px !important;
  width: 17px !important;
  }
  /* If the email client is reading the style element: */
  /* - then we don't need spacer divs */
  div.paragraph-spacer {
  display:none;
  height:0px !important;
  margin-bottom:0px !important;
  }
  /* - and margin-top already is in effect on #main */
  #apple-logo-margin-top {
  height:0px !important;
  }
  #logo-row-box {
  padding-top:0 !important;
  }
  /* div[dir="rtl"] #logo-row-box {
           text-align:left !important;
       } */
/* normally max-width: 320px */
@media ( max-width :320px) {
/* body[yahoo] prevents Yahoo! Mail from reading these rules, because it cannot read attribute selectors */
body[yahoo]#message {
-webkit-text-size-adjust: none;
}
body[yahoo] #apple-logo-left-margin {
width: 275px !important;
}
body[yahoo] #main {
margin-top: 18px;
padding-right: 0;
padding-left: 0;
}
body[yahoo] #apple-logo-in-row-box {
/* Not using hide and show approach between small and large imgs because Outlook Express 6 shows both imgs on reply */
/*
display:none !important;
height:0px !important;
width:0px !important;
*/
height: 20px !important;
width: 17px !important;
}
body[yahoo] #apple-logo-in-row-box-mobile {
/* display:inline-block !important; Not using hide and show approach between small and large imgs because Outlook Express 6 shows both imgs on reply */

}
body[yahoo] #apple-logo-margin-bottom {
height: 6px !important;
}
body[yahoo] #logo-row-box {
padding-bottom: 9px !important;
}
body[yahoo] p {
margin-bottom: 20px;
}
body[yahoo] td.paragraph {
padding: 0 0 20px !important;
}
body[yahoo] td.no-padding-bottom {
padding-bottom: 0 !important;
}
body[yahoo] p#signature {
margin-top: 36px !important;
margin-bottom: 28px !important;
}
body[yahoo] td#signature {
padding-top: 18px !important; /* was 36px */
padding-bottom: 28px !important;
}
body[yahoo] td#footer-links {
padding-bottom: 12px !important;
}
body[yahoo] #copyright #apple-address, body[yahoo] #copyright #all-rights-reserved
{
display: block;
}
body[yahoo] #left-align-on-reply {
/* moved from body */
padding-right: 16px;
padding-left: 16px;
width: 300px;
}
body[yahoo] footer {
font: 11px/15px 'Helvetica Neue', Helvetica, Geneva, Verdana, Arial,
sans-serif;
}
}
  /* typography-body */

.warning-list
  {
  font-size: 17px;
  line-height: 25px;
  font-weight: normal;
  font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  color: #333333;
  }

.email-header
  {
  font-size: 32px;
  line-height:36px;
  padding-bottom: 10px;
  border: 0 !important;
  }

.email-body
  {
  font-size: 17px;
  line-height: 25px;
  font-weight: normal;
  font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  color: #333333;
  }

  .email-signature
  {
  margin-top: 1.5em;
  }
  /* block-link */
  a
  {
  color: #0070c9;
  cursor: pointer;
  }
  a:link, a:visited
  {
  text-decoration: none;
  }

  .form-alert.form-alert-warning {
  border: 0;
  border-left: 6px solid #fee450;
  background-color: #fbf8e8!important;
  }
  .form-alert {
  border-radius: 4px;
  }
  .form-alert {
  font-size: 17px;
  line-height: 25px;
  font-weight: normal;
  font-family: SF Pro Text,SF Pro Icons,Helvetica Neue,Helvetica,Arial,sans-serif;
  background-color: hsla(0,0%,95%,.4);
  background-clip: padding-box;
  border: 1px solid #e3e3e3;
  padding: 15px 15px 7px 15px;
  margin-bottom: 20px;
  margin-top: 20px;
  }

.email-header
{
  font-size: 32px;
  line-height: 36px;
  font-weight: 500;
  font-family: "SF Pro Display", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  margin-bottom: 0.5em;
  text-align:center;
}

  </style>

</head>

<!-- body[yahoo] is being used to prevent Yahoo! Mail from reading these rules, because it cannot read attribute selectors -->
<body id="message" style="background-color:#fff;" yahoo="fix">
	<div id="left-align-on-reply" dir="ltr">
		<div id="main" style="margin-top: 40px;padding-right:15px;padding-left:15px;padding-bottom:30px;">
			<!--<div id="apple-logo-margin-top" style="height:40px;"></div>-->
						 <div id="logo-row-box" style="width:95%;text-align:left ;padding-top:6%;padding-bottom:6%;">
        <img id="apple-logo-in-row-box" src="https://s21.ax1x.com/2024/07/30/pkLTB4A.png" style="display:inline-block;height:24px;width:20px;right:0px;" alt=“Apple”>
        <!--<img id="apple-logo-in-row-box-mobile" src="https://statici.icloud.com/emailimages/v4/common/apple_logo_web.png" style="display:none;height:0;width:0;right:0px;" height="0" width="0">-->
        <!--Two logos are appearing on reply in Windows XP Outlook-->
      </div>
			 <div class="container">
<h1 class="email-header" style="font-size:32px;line-height:36px;font-weight:500;padding-bottom:10px;color:#333;text-align:center;">验证您的 TDesigner 账号电子邮件地址</h1>
			<div class="email-body" style="font-size:17px;line-height:25px;color:#333;font-weight:normal;">
									<p></p>						<p>您已选择此电子邮件地址作为您的 <span style="white-space: nowrap">TDesigner</span> 账号的电子邮箱。为验证此电子邮件地址属于您，请在电子邮件验证页面输入下方验证码：</p>
<div class="email-body" style="font-size:23px;line-height:25px;color:#333;font-weight:normal;">
						<p><b>verify_code</b></p></div>
						<p>验证码会在客户端关闭后失效。</p>
						<p><b>您收到此电子邮件的原因：</b><br>
						TDesigner 会在您选择一电子邮件地址时对其进行验证。验证电子邮件地址后，您才能使用 <span style="white-space: nowrap">TDesigner</span>。</p>
						<p>如果您未提出此请求，您可以忽略这封电子邮件。<span style="white-space: nowrap">TDesigner</span> 账号只有在验证后才能创建。</p>
																		<p class="email-signature"></p>
			 </div>
      		</div>		
		</div><!--end #main -->
		<footer style="width:100%; background-color: #f2f2f2;">
       <table id="footer-paragraphs" width="100%" border="0" cellpadding="0" cellspacing="0" style="background:#f2f2f2; padding:20px 15px 20px 15px;">

           <tr>
               <td id="footer-links" style="padding:0;font-size:12px;line-height:18px;color:#888 !important;">

TDesigner

</td>
</tr>

           <tr>

<td id="copyright-cell" style="padding:0;font-size:12px;line-height:18px;color:#888 !important;">Copyright © BUAA <span id="apple-address" class="unlink">2206</span> <span id="all-rights-reserved" style="white-space:nowrap;">仅供学习使用。</span>
</td>

</tr>

       </table>
</footer>
</div><!--end #left-align-on-reply-->
</body>
</html>
"""