
 


<!DOCTYPE html>
<html lang="en">
<head>
 <link rel="icon" type="image/vnd.microsoft.icon" href="/static/images/monorail.ico">
 
 <script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
 
 window.CS_env = {
 'absoluteBaseUrl': 'https://bugs.chromium.org',
 'app_version': 'monorail-prod-default-v069.427094976126226458',
 'token': 'xRJ_ibo6ELlTJIt3gxBbsDoxNTkxMjAwNjM4',
 'tokenExpiresSec': 1591207538,
 'loggedInUserEmail':
 
 null
 ,
 'login_url': 'https://accounts.google.com/ServiceLogin?service\x3dah\x26passive\x3dtrue\x26continue\x3dhttps://appengine.google.com/_ah/conflogin%3Fcontinue%3Dhttps://bugs.chromium.org/p/project-zero/issues/list',
 'logout_url': 'https://bugs.chromium.org/_ah/logout?continue\x3dhttps://accounts.google.com/Logout%3Fcontinue%3Dhttps://appengine.google.com/_ah/logout%253Fcontinue%253Dhttps://google.com/url%25253Fsa%25253DD%252526q%25253Dhttps://bugs.chromium.org/p/project-zero/issues/list%252526ust%25253D1591287038042826%252526usg%25253DAFQjCNFGx7e2uCJP_ERq9ZB0aDe3DzhGuw%26service%3Dah',
 'profileUrl':
 
 null
 ,
 'projectName': 'project-zero',
 'projectIsRestricted': false,
 'is_member': '',
 'gapi_client_id': '679746765624-tqaakho939p2mc7eb65t4ecrj3gj08rt.apps.googleusercontent.com',
 };
 </script>
 
 
 <title>
 Monorail - 
 
 
 project-zero -
 
 
 Project Zero - 
 
 Monorail
 </title>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
 <meta name="referrer" content="no-referrer">
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <meta name="viewport" content="width=device-width, minimum-scale=1.0">
 <link type="text/css" rel="stylesheet" href="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/css/chopsui-normal.css">
 
 <!-- Lazy load icons. -->
 <link rel="stylesheet"
 href="https://fonts.googleapis.com/icon?family=Material+Icons"
 media="none"
 id="icons-stylesheet">
 <script type="module" async defer nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
 document.getElementById('icons-stylesheet').media = 'all';
 </script>
 
</head>
<script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
 function _go(url, newWindow) {
 if (newWindow)
 window.open(url, '_blank');
 else
 document.location = url;
 }
 function $(id) { return document.getElementById(id); }
 var loadQueue = [];
 function runOnLoad(fn) { loadQueue.push(fn); }
 window.onload = function() {
 for (var i = 0; i < loadQueue.length; i++)
 loadQueue[i]();
 delete loadQueue;
 };
</script>

<!-- This is a webpack-generated ezt template for script tags. -->
<!-- Do not edit or commit to repo. -->
<script type="module" src="/static/dist/mr-app.9b55b05c15486a86987e.min.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<mr-app 
 loginUrl="https://accounts.google.com/ServiceLogin?service=ah&amp;passive=true&amp;continue=https://appengine.google.com/_ah/conflogin%3Fcontinue%3Dhttps://bugs.chromium.org/p/project-zero/issues/list"
 logoutUrl="https://bugs.chromium.org/_ah/logout?continue=https://accounts.google.com/Logout%3Fcontinue%3Dhttps://appengine.google.com/_ah/logout%253Fcontinue%253Dhttps://google.com/url%25253Fsa%25253DD%252526q%25253Dhttps://bugs.chromium.org/p/project-zero/issues/list%252526ust%25253D1591287038042826%252526usg%25253DAFQjCNFGx7e2uCJP_ERq9ZB0aDe3DzhGuw%26service%3Dah"
 versionBase="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com"
></mr-app>

<div id="footer">
 
 <a href="https://bugs.chromium.org/p/project-zero/issues/list_old">
 View in the old UI
 </a>
 
 <a href="https://bugs.chromium.org/p/monorail/adminIntro" title="Monorail monorail-prod-default-v069.427094976126226458">About Monorail</a>
 <a href="https://chromium.googlesource.com/infra/infra/+/master/appengine/monorail/doc/userguide/README.md">User Guide</a>
 <a href="https://chromium.googlesource.com/infra/infra/+/master/appengine/monorail/doc/release-notes.md">Release Notes</a>
 <a href="https://bugs.chromium.org/p/monorail/issues/entry" target="_blank">Feedback on Monorail</a>
 <a href="https://chromium.googlesource.com/infra/infra/+/master/appengine/monorail/doc/terms.md">Terms</a>
 <a href="https://www.google.com/policies/privacy/">Privacy</a>
</div>

 


<!-- This is a webpack-generated ezt template for script tags. -->
<!-- Do not edit or commit to repo. -->
<script type="module" src="/static/dist/ezt-footer-scripts-package.d295881d5446f9ec1fc7.min.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="module" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
// Load and instantiate pRPC client before any other script.
window.prpcClient = new AutoRefreshPrpcClient(
 CS_env.token, CS_env.tokenExpiresSec);
</script>
<script type="text/javascript"
 src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/deployed_node_modules/@webcomponents/webcomponentsjs/webcomponents-bundle.js"
 nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"
></script>


<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/common.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/listen.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/xmlhttp.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/shapes.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/geom.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/graveyard/popup_controller.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>

<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/tracker/ac.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/tracker/tracker-ac.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>
<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/tracker/tracker-install-ac.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>

<script type="text/javascript" defer src="https://monorail-prod-default-v069-dot-monorail-prod.appspot.com/static/js/tracker/tracker-editing.js" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu"></script>


 <script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
 runOnLoad(function() {
 TKR_install_ac();
 });
 </script>

<script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
runOnLoad(function() {
 // CrDX Feedback Button
 (function(i,s,o,g,r,a,m){i['CrDXObject']=r;i[r]=i[r]||function(){
 (i[r].q=i[r].q||[]).push(arguments)},a=s.createElement(o),
 m=s.getElementsByTagName(o)[0];a.async=1;a.setAttribute('nonce','pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu');
 a.src=g;m.parentNode.insertBefore(a,m)
 })(window,document,'script','https://storage.googleapis.com/crdx-feedback.appspot.com/feedback.js','crdx');
 crdx('setFeedbackButtonLink', 'https://bugs.chromium.org/p/monorail/issues/entry?template=Online%20Feedback');
});
</script>

<script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.setAttribute('nonce','pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu');
a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
(function setupGoogleAnalytics() {
 ga('create', 'UA-55762617-14', {'siteSpeedSampleRate': 100});
})();
</script>


<script type="text/javascript" nonce="pgdydqexkarkUEyaXEBDYVkXN8Ddv5vu">
 runOnLoad(function() {
 if (typeof(ClientLogger) === "function") {
 let cl = new ClientLogger("issues");
 if (cl.started("new-issue")) {
 cl.logEnd("new-issue", null, 120 * 1000);
 }
 if (cl.started("issue-search")) {
 cl.logEnd("issue-search");
 }
 }
 });
</script>
