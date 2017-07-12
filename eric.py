from bs4 import BeautifulSoup
from requests import get
from time import sleep
from selenium import webdriver
from dateutil import parser

test = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="cs"><head><script src="https://apis.google.com/_/scs/apps-static/_/js/k=oz.gapi.en_US.vapb4E2BnWs.O/m=auth/exm=plusone/rt=j/sv=1/d=1/ed=1/am=AQ/rs=AGLTcCOY6I79W2gOngQhoBDIFvlI0EnkcA/cb=gapi.loaded_1" async=""></script><script src="https://apis.google.com/_/scs/apps-static/_/js/k=oz.gapi.en_US.vapb4E2BnWs.O/m=plusone/rt=j/sv=1/d=1/ed=1/am=AQ/rs=AGLTcCOY6I79W2gOngQhoBDIFvlI0EnkcA/cb=gapi.loaded_0" async=""></script><script type="text/javascript" async="" src="http://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://apis.google.com/js/plusone.js" gapi_processed="true"></script><script id="facebook-jssdk" async="" src="//connect.facebook.net/en_US/all.js#xfbml=1&amp;appId=393736670647047"></script>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="expires" content="Thu, 01 Jan 1970 00:59:59 GMT" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta property="og:type" content="sport" />
    <meta property="og:image" content="http://www.oddsportal.com/oddsportal.png" />
    <meta property="og:site_name" content="Oddsportal.com" />
    <link rel="image_src" href="http://www.oddsportal.com/oddsportal.png" />
    <!-- APPLE TOUCH ICONS -->
    <link rel="apple-touch-icon" href="/res/img/apple-touch-icon.png" alt="Iphone icon" />
    <link rel="apple-touch-icon" sizes="72x72" href="/res/img/apple-touch-icon-72x72.png" alt="Ipad icon" />
    <link rel="apple-touch-icon" sizes="114x114" href="/res/img/apple-touch-icon-114x114.png" alt="Iphone, Ipad Hi icon" />
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="canonical" href="http://www.oddsportal.com/basketball/usa/nba-las-vegas-summer-league-2013/results/" />
    <script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-W3GJZ5"></script><script type="text/javascript">
        //&lt;![CDATA[
        function CTIsPlayback()
        {
            try
            {
                return parent &amp;&amp; parent.WebPlayer;
            } catch (e)
            {
                return false;
            }
        }
        if (!CTIsPlayback())
        {
            if (top != self)
            {
                top.location.replace(self.location.href);
            }
        }    //]]&gt;
    </script>

                    <meta name="author" content="LiveSport s.r.o." />
                                <meta name="copyright" content="(c) LiveSport s.r.o. 2007 - 2017" />
                                <meta name="robots" content="index,follow" />
                                <meta name="verify-v1" content="Bb7e33T56Ylh3AuhM08L41r1bjNsdEchyFEqQPnK2wg=" />
                                <meta name="description" content="Archived betting odds and match results from NBA Las Vegas Summer League 2013. Archived results guide you through the basketball NBA Las Vegas Summer League 2013 historical results and winning odds." />
                                <meta name="keywords" content="odds portal, odds comparison, archive, historical odds, results, betting odds, odds archive" />
                    <title>NBA Las Vegas Summer League 2013 Results &amp; Historical Odds, Basketball USA Archive</title>

    <script type="text/javascript" src="/ajax-userdata/?1499870083e7acfd79777f2e49cfd3c2e803c44a3b"></script>
        <link rel="Stylesheet" href="/res/x/global-170712150043.css" type="text/css" media="screen, projection" />
    <link rel="Stylesheet" href="/res/x/bookmakers-170712150043-1499865132.css" type="text/css" media="screen, projection" />
    <!--[if IE]>
    <link rel="Stylesheet" href="/res/x/ie-170712150043.css" type="text/css" media="screen, projection"/>
    <![endif]-->
        <script type="text/javascript" src="/res/x/global-170712150043.js"></script>
    <script type="text/javascript" src="/res/x/bookies-170712150043-1499865132.js"></script>


    <script type="text/javascript" src="/res/x/jsxcompressor-170712150043.js"></script>
    <script type="text/javascript" src="/res/x/pushclient-170712150043.js"></script>

    <script type="text/javascript">
        var _loadTime = (new Date()).getTime();
    </script>
    <!--[if IE]>
    <script type="text/javascript">
        // <![CDATA[
        try { document.execCommand("BackgroundImageCache", false, true); } catch(err) {}
    // ]]>
    </script>
<![endif]-->


    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&amp;l='+l:'';j.async=true;j.src=
            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-W3GJZ5');</script>
    <!-- End Google Tag Manager -->


<style type="text/css">.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:"lucida grande", tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset&gt;div{overflow:hidden}.fb_link img{border:none}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_dialog{background:rgba(82, 82, 82, .7);position:absolute;top:-10000px;z-index:10001}.fb_reset .fb_dialog_legacy{overflow:visible}.fb_dialog_advanced{padding:10px;-moz-border-radius:8px;-webkit-border-radius:8px;border-radius:8px}.fb_dialog_content{background:#fff;color:#333}.fb_dialog_close_icon{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 0 transparent;cursor:pointer;display:block;height:15px;position:absolute;right:18px;top:17px;width:15px}.fb_dialog_mobile .fb_dialog_close_icon{top:5px;left:5px;right:auto}.fb_dialog_padding{background-color:transparent;position:absolute;width:1px;z-index:-1}.fb_dialog_close_icon:hover{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -15px transparent}.fb_dialog_close_icon:active{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -30px transparent}.fb_dialog_loader{background-color:#f6f7f9;border:1px solid #606060;font-size:24px;padding:20px}.fb_dialog_top_left,.fb_dialog_top_right,.fb_dialog_bottom_left,.fb_dialog_bottom_right{height:10px;width:10px;overflow:hidden;position:absolute}.fb_dialog_top_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 0;left:-10px;top:-10px}.fb_dialog_top_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -10px;right:-10px;top:-10px}.fb_dialog_bottom_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -20px;bottom:-10px;left:-10px}.fb_dialog_bottom_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -30px;right:-10px;bottom:-10px}.fb_dialog_vert_left,.fb_dialog_vert_right,.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{position:absolute;background:#525252;filter:alpha(opacity=70);opacity:.7}.fb_dialog_vert_left,.fb_dialog_vert_right{width:10px;height:100%}.fb_dialog_vert_left{margin-left:-10px}.fb_dialog_vert_right{right:0;margin-right:-10px}.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{width:100%;height:10px}.fb_dialog_horiz_top{margin-top:-10px}.fb_dialog_horiz_bottom{bottom:0;margin-bottom:-10px}.fb_dialog_iframe{line-height:0}.fb_dialog_content .dialog_title{background:#6d84b4;border:1px solid #365899;color:#fff;font-size:14px;font-weight:bold;margin:0}.fb_dialog_content .dialog_title&gt;span{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/Cou7n-nqK52.gif) no-repeat 5px 50%;float:left;padding:5px 0 7px 26px}body.fb_hidden{-webkit-transform:none;height:100%;margin:0;overflow:visible;position:absolute;top:-10000px;left:0;width:100%}.fb_dialog.fb_dialog_mobile.loading{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/3rhSv5V8j3o.gif) white no-repeat 50% 50%;min-height:100%;min-width:100%;overflow:hidden;position:absolute;top:0;z-index:10001}.fb_dialog.fb_dialog_mobile.loading.centered{width:auto;height:auto;min-height:initial;min-width:initial;background:none}.fb_dialog.fb_dialog_mobile.loading.centered #fb_dialog_loader_spinner{width:100%}.fb_dialog.fb_dialog_mobile.loading.centered .fb_dialog_content{background:none}.loading.centered #fb_dialog_loader_close{color:#fff;display:block;padding-top:20px;clear:both;font-size:18px}#fb-root #fb_dialog_ipad_overlay{background:rgba(0, 0, 0, .45);position:absolute;bottom:0;left:0;right:0;top:0;width:100%;min-height:100%;z-index:10000}#fb-root #fb_dialog_ipad_overlay.hidden{display:none}.fb_dialog.fb_dialog_mobile.loading iframe{visibility:hidden}.fb_dialog_content .dialog_header{-webkit-box-shadow:white 0 1px 1px -1px inset;background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#738ABA), to(#2C4987));border-bottom:1px solid;border-color:#1d4088;color:#fff;font:14px Helvetica, sans-serif;font-weight:bold;text-overflow:ellipsis;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0;vertical-align:middle;white-space:nowrap}.fb_dialog_content .dialog_header table{-webkit-font-smoothing:subpixel-antialiased;height:43px;width:100%}.fb_dialog_content .dialog_header td.header_left{font-size:12px;padding-left:5px;vertical-align:middle;width:60px}.fb_dialog_content .dialog_header td.header_right{font-size:12px;padding-right:5px;vertical-align:middle;width:60px}.fb_dialog_content .touchable_button{background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#4966A6), color-stop(.5, #355492), to(#2A4887));border:1px solid #29487d;-webkit-background-clip:padding-box;-webkit-border-radius:3px;-webkit-box-shadow:rgba(0, 0, 0, .117188) 0 1px 1px inset, rgba(255, 255, 255, .167969) 0 1px 0;display:inline-block;margin-top:3px;max-width:85px;line-height:18px;padding:4px 12px;position:relative}.fb_dialog_content .dialog_header .touchable_button input{border:none;background:none;color:#fff;font:12px Helvetica, sans-serif;font-weight:bold;margin:2px -12px;padding:2px 6px 3px 6px;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog_content .dialog_header .header_center{color:#fff;font-size:16px;font-weight:bold;line-height:18px;text-align:center;vertical-align:middle}.fb_dialog_content .dialog_content{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat 50% 50%;border:1px solid #555;border-bottom:0;border-top:0;height:150px}.fb_dialog_content .dialog_footer{background:#f6f7f9;border:1px solid #555;border-top-color:#ccc;height:40px}#fb_dialog_loader_close{float:left}.fb_dialog.fb_dialog_mobile .fb_dialog_close_button{text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog.fb_dialog_mobile .fb_dialog_close_icon{visibility:hidden}#fb_dialog_loader_spinner{animation:rotateSpinner 1.2s linear infinite;background-color:transparent;background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/t-wz8gw1xG1.png);background-repeat:no-repeat;background-position:50% 50%;height:24px;width:24px}@keyframes rotateSpinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.fb_iframe_widget{display:inline-block;position:relative}.fb_iframe_widget span{display:inline-block;position:relative;text-align:justify}.fb_iframe_widget iframe{position:absolute}.fb_iframe_widget_fluid_desktop,.fb_iframe_widget_fluid_desktop span,.fb_iframe_widget_fluid_desktop iframe{max-width:100%}.fb_iframe_widget_fluid_desktop iframe{min-width:220px;position:relative}.fb_iframe_widget_lift{z-index:1}.fb_hide_iframes iframe{position:relative;left:-10000px}.fb_iframe_widget_loader{position:relative;display:inline-block}.fb_iframe_widget_fluid{display:inline}.fb_iframe_widget_fluid span{width:100%}.fb_iframe_widget_loader iframe{min-height:32px;z-index:2;zoom:1}.fb_iframe_widget_loader .FB_Loader{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat;height:32px;width:32px;margin-left:-16px;position:absolute;left:50%;z-index:4}</style></head>
<body>


    <!-- Google Tag Manager (noscript) -->
    <noscript>&lt;iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W3GJZ5" height="0" width="0" style="display:none;visibility:hidden"&gt;&lt;/iframe&gt;</noscript>
    <!-- End Google Tag Manager (noscript) -->




<div class="wrap">

<div id="mother-main">

            <div id="top-right-social-column">
                <div id="top-right-social-column-child">
                    <div id="___plusone_0" style="text-indent: 0px; margin: 0px; padding: 0px; background: transparent; border-style: none; float: none; line-height: normal; font-size: 1px; vertical-align: baseline; display: inline-block; width: 90px; height: 20px;"><iframe ng-non-bindable="" frameborder="0" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="position: static; top: 0px; width: 90px; margin: 0px; border-style: none; left: 0px; visibility: visible; height: 20px;" tabindex="0" vspace="0" width="100%" id="I0_1499870406926" name="I0_1499870406926" src="https://apis.google.com/se/0/_/+1/fastbutton?usegapi=1&amp;size=medium&amp;origin=http%3A%2F%2Fwww.oddsportal.com&amp;url=http%3A%2F%2Fwww.oddsportal.com%2F&amp;gsrc=3p&amp;ic=1&amp;jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.en_US.vapb4E2BnWs.O%2Fm%3D__features__%2Fam%3DAQ%2Frt%3Dj%2Fd%3D1%2Frs%3DAGLTcCOY6I79W2gOngQhoBDIFvlI0EnkcA#_methods=onPlusOne%2C_ready%2C_close%2C_open%2C_resizeMe%2C_renderstart%2Concircled%2Cdrefresh%2Cerefresh%2Conload&amp;id=I0_1499870406926&amp;parent=http%3A%2F%2Fwww.oddsportal.com&amp;pfname=&amp;rpctoken=22487893" data-gapiattached="true" title="+1"></iframe></div>
                    <div class="fb-like fb_iframe_widget" data-href="http://www.facebook.com/OddsPortal" data-layout="button_count" data-action="like" data-show-faces="true" data-share="false" style="margin-top:3px;" fb-xfbml-state="rendered" fb-iframe-plugin-query="action=like&amp;app_id=393736670647047&amp;container_width=90&amp;href=http%3A%2F%2Fwww.facebook.com%2FOddsPortal&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;share=false&amp;show_faces=true"><span style="vertical-align: bottom; width: 74px; height: 20px;"><iframe name="f5673f334fdc68" width="1000px" height="1000px" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" title="fb:like Facebook Social Plugin" src="https://www.facebook.com/plugins/like.php?action=like&amp;app_id=393736670647047&amp;channel=http%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter%2Fr%2FXBwzv5Yrm_1.js%3Fversion%3D42%23cb%3Df159186f39379d8%26domain%3Dwww.oddsportal.com%26origin%3Dhttp%253A%252F%252Fwww.oddsportal.com%252Ff2251d3f810fccc%26relation%3Dparent.parent&amp;container_width=90&amp;href=http%3A%2F%2Fwww.facebook.com%2FOddsPortal&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;share=false&amp;show_faces=true" style="border: none; visibility: visible; width: 74px; height: 20px;" class=""></iframe></span></div>
                </div>
            </div>
        
<div id="mother">
<div class="adsenvelope adstextvpad banx-header" id="lsadvert-zid-1877" style="width:970px;"><div style="height:90px"><div class="adscontent" id="lsadvert-header"><iframe id="lsadvert-zid-1877-iframe" name="banx-header" frameborder="0" scrolling="no" style="width: 970px; height: 90px;"></iframe></div><div class="adsgraphvert"><div class="adsgvert atv-en"></div></div></div></div><div class="adsclear"></div><div id="header">

    <div id="nav-skip">
        <a href="#col-content" accesskey="2" title="Proceed to content (Keyboard shortcut: Alt + 2)">Proceed to content</a>
         | 
        <a href="#main-menu">Proceed to main menu</a>
         | 
        <a href="#search-box">Proceed to search</a>

        <hr class="hidden" />
    </div>

    <div id="logo-box">
        <p>
            <a href="/">
                <img src="http://rb.oddsportal.com/img/logo-odds-portal.png" width="293" height="39" alt="ODDS Portal" />
            </a>
        </p>

        <hr class="hidden" />
    </div>

    <div id="user-header">
        <div id="user-header-r1">
            <div>
                <a class="user-header-fakeselect" onclick="ElementSelect.expand( 'user-header-oddsformat' , 'user-header-oddsformat-expander' )" id="user-header-oddsformat-expander"><span>EU Odds</span></a>
                <ul class="user-header-fakeselect-options hidden" id="user-header-oddsformat">
                    <li><a href="#" onclick="changeOddsFormat(1); return false;"><span>EU Odds</span></a></li>
                    <li><a href="#" onclick="changeOddsFormat(2); return false;"><span>UK Odds</span></a></li>
                    <li><a href="#" onclick="changeOddsFormat(3); return false;"><span>US Odds</span></a></li>
                    <li><a href="#" onclick="changeOddsFormat(4); return false;"><span>HK Odds</span></a></li>
                    <li><a href="#" onclick="changeOddsFormat(5); return false;"><span>MA Odds</span></a></li>
                    <li><a href="#" onclick="changeOddsFormat(6); return false;"><span>IN Odds</span></a></li>

                </ul>
            </div>
            <div><label>Time:</label></div>
            <div>
                <a href="#" class="user-header-fakeselect" onclick="op.showHideTimeZone();ElementSelect.expand( 'user-header-timezone' , 'user-header-timezone-expander' , null , function(){op.hideTimeZone()} );this.blur();return false;" id="user-header-timezone-expander"><span>12 Jul 14:40, GMT 0</span></a>
            </div>


        </div><form id="user-header-r2" action="/" method="post"><div><label for="login-username">Username:</label></div><div><input type="text" id="login-username" name="login-username" value="" /></div><div><label for="login-password">Password:</label></div><div><input type="password" id="login-password" name="login-password" /></div><div class="fix"><button class="inline-btn-2 r button-dark" name="login-submit" type="submit"><span><span>Login</span></span></button></div><div><button class="inline-btn-2 r button-red2" onclick="document.location = '/register/';" type="button"><span><span>REGISTER</span></span></button></div></form>

        

    </div>

    <div class="break"></div>
</div>

<div id="main-menu">
    <h2 class="out">Main menu</h2>
    <!-- TOP MENU -->
    <ul>
        <li class="active">
                        <strong><span><a href="/" id="main-odds-comparison_2">Odds Comparison</a></span></strong>
                            <div class="sub-menu">
                                <ul><li><a href="/" id="main-home-odds-home_3">Home</a></li><li><a href="/matches/" id="main-next-games_7">Next Matches</a></li><li><a href="/dropping-odds/" id="main-dropping-odds_43">Dropping Odds</a></li><li><a href="/sure-bets/" id="main-sure-bets_25">Sure Bets</a></li><li><a href="/inplay-odds/" id="main-next-games-live_64">In-Play Odds</a></li><li><a href="/events/" id="main-all-events_44">All Events</a></li><li class="select select-hover"><ul><li><a href="/blocked/" id="main-blocked-games_41">Blocked Odds</a></li><li><a href="/value-bets/" id="main-value-bets_24">Value Bets</a></li><li><a href="/hot-matches/" id="main-hot-matches_33">Hot Matches</a></li><li><a href="/handicaps/" id="main-divergent-margins_54">Best Handicaps</a></li><li><a href="/moving-margins/" id="main-moving-margins_55">Moving Margins</a></li><li><a href="/results/" id="main-odds-archive_47">Archived Results</a></li><li><a href="/standings/" id="main-all-events-standings_81">Standings</a></li></ul><a class="dropdowner" id="main-betting-tools_87">Betting tools</a></li></ul>
            <div class="break"></div>
            </div>
            </li><li><a href="/community/" id="community-main_90"><span>Community</span></a></li><li><a href="/livescores/" id="main-live-scores_6"><span>Live Scores</span></a></li><li class="last"><a href="/bookmakers/" id="main-bookmakers_5"><span>Bookmakers</span></a></li>    </ul>

    <!-- END TOP MENU -->
    <div class="break"></div>
    <hr class="hidden" />
</div>

            <div id="right-ad-column">
                <div class="scrolling-banner-top-stop"></div>
                <div class="scrolling-banner-wrap" style="left: 1020px;">
                    <div id="right-ad-column-child">
                        <div class="adsenvelope banx-RS1" id="lsadvert-zid-523" style="width:202px;"><div style="height:600px"><div class="adscontent" id="lsadvert-RS1"><iframe id="lsadvert-zid-523-iframe" name="banx-RS1" frameborder="0" scrolling="no" style="width: 202px; height: 600px;"></iframe></div></div></div><div class="adstext"><span>advertisement</span></div>                  </div>
                </div>
            </div>
            
<div id="wrap">
    <div id="box-top">
        <div id="box-bottom">
            <div id="main" class="home">
                <div id="breadcrumb">
                    <h2 class="out">You are here</h2>
                     <a href="/">Home</a> » <a href="/basketball/">Basketball</a> » <a href="/basketball/usa/">USA</a> » <a href="/basketball/usa/nba-las-vegas-summer-league-2013/results/">NBA Las Vegas Summer League 2013</a> »
                                                                NBA Las Vegas Summer League 2013 Odds                                           
                </div>

                <hr class="hidden" />
                            <div id="col-left">
                <div id="col-content">
                    <h1>NBA Las Vegas Summer League 2013 Results &amp; Historical Odds</h1><div class="message-info"><ul><li><div class="cms">We have noticed that you may be located in a different time zone. You may want to change the time zone here <a href="/set-timezone/15/"> to GMT -4</a> or click the time zone selector at the top right corner.</div></li></ul></div>                    <!-- PAGE BODY -->
                    <div class="main-menu2 menu-round" id="tournament_menu"><ul class="main-filter"><li><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2013/">NEXT MATCHES</a></strong></span></li><li><span class="active"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2013/results/">RESULTS</a></strong></span></li><li class="standings"><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2013/standings/">STANDINGS</a></strong></span></li></ul></div><div class="break5"></div><div class="main-menu2 main-menu-gray"><ul class="main-filter"><li><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league/results/">2017</a></strong></span></li><li><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2016/results/">2016</a></strong></span></li><li><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2015/results/">2015</a></strong></span></li><li><span class="inactive"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2014/results/">2014</a></strong></span></li><li><span class="active"><strong><a href="/basketball/usa/nba-las-vegas-summer-league-2013/results/">2013</a></strong></span></li></ul></div><div class="break5"></div><div class="box"><div class="tab-nav-line-margin"></div></div><div id="tournamentTable" style="display: block;"><table class=" table-main" id="tournamentTable"><colgroup><col width="50" /><col width="*" /><col width="50" /><col width="50" /><col width="50" /><col width="50" /><col width="50" /></colgroup><tbody><tr class="dark center" xtid="16153"><th class="first2 tl" colspan="7"><a class="bfl sicona s3" href="/basketball/">Basketball</a><span class="bflp">»</span><a class="bfl" href="/basketball/usa/"><span class="ficon f-200"> </span>USA</a><span class="bflp">»</span><a href="/basketball/usa/nba-las-vegas-summer-league-2013/">NBA Las Vegas Summer League 2013</a></th></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374541200-2-0-0-1">23 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="W8Slwk8p"><td class="table-time datet t1374541200-1-1-0-0 ">01:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/golden-state-warriors-phoenix-suns-W8Slwk8p/"><span class="bold">Golden State Warriors</span> - Phoenix Suns</a></td><td class="center bold table-odds table-score">91:77</td><td class="result-ok odds-nowrp" xoid="E-1ldqax2rrhkx0x3aam0" xodd="azppfazpa"><a href="" onclick="globals.ch.togle(this , 'E-1ldqax2rrhkx0x3aam0');return false;" xparam="odds_text">1.71</a></td><td class="odds-nowrp" xoid="E-1ldqax2rrhkx0x3aam1" xodd="xzxefxzat"><a href="" onclick="globals.ch.togle(this , 'E-1ldqax2rrhkx0x3aam1');return false;" xparam="odds_text">2.14</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374451200-2-0-0-1">22 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="rJQNdMRk"><td class="table-time datet t1374451200-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/golden-state-warriors-charlotte-hornets-rJQNdMRk/"><span class="bold">Golden State Warriors</span> - Charlotte Hornets</a></td><td class="center bold table-odds table-score">75:67</td><td class="result-ok odds-nowrp" xoid="E-1lcclx2rrhkx0x3a7q8" xodd="az8efazpc"><a href="" onclick="globals.ch.togle(this , 'E-1lcclx2rrhkx0x3a7q8');return false;" xparam="odds_text">1.73</a></td><td class="odds-nowrp" xoid="E-1lcclx2rrhkx0x3a7q9" xodd="xzxfxzaa"><a href="" onclick="globals.ch.togle(this , 'E-1lcclx2rrhkx0x3a7q9');return false;" xparam="odds_text">2.11</a></td><td class="center info-value">9</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374444000-2-0-0-1">21 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="Yici1sIr"><td class="table-time datet t1374444000-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/phoenix-suns-miami-heat-Yici1sIr/"><span class="bold">Phoenix Suns</span> - Miami Heat</a></td><td class="center bold table-odds table-score">91:89</td><td class="result-ok odds-nowrp" xoid="E-1lcanx2rrhkx0x3a7kk" xodd="azpefazox"><a href="" onclick="globals.ch.togle(this , 'E-1lcanx2rrhkx0x3a7kk');return false;" xparam="odds_text">1.62</a></td><td class="odds-nowrp" xoid="E-1lcanx2rrhkx0x3a7kl" xodd="xzoefxzcx"><a href="" onclick="globals.ch.togle(this , 'E-1lcanx2rrhkx0x3a7kl');return false;" xparam="odds_text">2.32</a></td><td class="center info-value">9</td></tr><tr class=" deactivate" xeid="xh6Vv19A"><td class="table-time datet t1374372000-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/golden-state-warriors-los-angeles-lakers-xh6Vv19A/"><span class="bold">Golden State Warriors</span> - Los Angeles Lakers</a></td><td class="center bold table-odds table-score">83:77</td><td class="result-ok odds-nowrp" xoid="E-1l90ex2rrhkx0x3a0us" xodd="azpfazoe"><a href="" onclick="globals.ch.togle(this , 'E-1l90ex2rrhkx0x3a0us');return false;" xparam="odds_text">1.65</a></td><td class="odds-nowrp" xoid="E-1l90ex2rrhkx0x3a0ut" xodd="xztefxzxp"><a href="" onclick="globals.ch.togle(this , 'E-1l90ex2rrhkx0x3a0ut');return false;" xparam="odds_text">2.27</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="4do4HNIF"><td class="table-time datet t1374364800-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/nba-d-league-charlotte-hornets-4do4HNIF/">NBA D-League - <span class="bold">Charlotte Hornets</span></a></td><td class="center bold table-odds table-score">75:85</td><td class="odds-nowrp" xoid="E-1l8nbx2rrhkx0x3a0cj" xodd="azpfazoo"><a href="" onclick="globals.ch.togle(this , 'E-1l8nbx2rrhkx0x3a0cj');return false;" xparam="odds_text">1.66</a></td><td class="result-ok odds-nowrp" xoid="E-1l8nbx2rrhkx0x3a0ci" xodd="xztofxzxt"><a href="" onclick="globals.ch.togle(this , 'E-1l8nbx2rrhkx0x3a0ci');return false;" xparam="odds_text">2.24</a></td><td class="center info-value">6</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374357600-2-0-0-1">20 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="jgs0I339"><td class="table-time datet t1374357600-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/phoenix-suns-toronto-raptors-jgs0I339/"><span class="bold">Phoenix Suns</span> - Toronto Raptors</a></td><td class="center bold table-odds table-score">103:98</td><td class="result-ok odds-nowrp" xoid="E-1l8nax2rrhkx0x3a0cg" xodd="azpfazot"><a href="" onclick="globals.ch.togle(this , 'E-1l8nax2rrhkx0x3a0cg');return false;" xparam="odds_text">1.64</a></td><td class="odds-nowrp" xoid="E-1l8nax2rrhkx0x3a0ch" xodd="xzttfxzc"><a href="" onclick="globals.ch.togle(this , 'E-1l8nax2rrhkx0x3a0ch');return false;" xparam="odds_text">2.30</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="djjekKiD"><td class="table-time datet t1374350400-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/cleveland-cavaliers-miami-heat-djjekKiD/">Cleveland Cavaliers - <span class="bold">Miami Heat</span></a></td><td class="center bold table-odds table-score">76:82</td><td class="odds-nowrp" xoid="E-1l8pnx2rrhkx0x3a0ha" xodd="az9afazp9"><a href="" onclick="globals.ch.togle(this , 'E-1l8pnx2rrhkx0x3a0ha');return false;" xparam="odds_text">1.79</a></td><td class="result-ok odds-nowrp" xoid="E-1l8pnx2rrhkx0x3a0hb" xodd="xzafxz0c"><a href="" onclick="globals.ch.togle(this , 'E-1l8pnx2rrhkx0x3a0hb');return false;" xparam="odds_text">2.03</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374287400-2-0-0-1">20 Jul 2013</span> - Losers Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="tj6H0Gh6"><td class="table-time datet t1374287400-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/minnesota-timberwolves-portland-trail-blazers-tj6H0Gh6/"><span class="bold">Minnesota Timberwolves</span> - Portland Trail Blazers</a></td><td class="center bold table-odds table-score">72:66</td><td class="result-ok odds-nowrp" xoid="E-1l9r2x2rrhkx0x3a2km" xodd="aztefaztc"><a href="" onclick="globals.ch.togle(this , 'E-1l9r2x2rrhkx0x3a2km');return false;" xparam="odds_text">1.43</a></td><td class="odds-nowrp" xoid="E-1l9r2x2rrhkx0x3a2kn" xodd="xz9efxz8a"><a href="" onclick="globals.ch.togle(this , 'E-1l9r2x2rrhkx0x3a2kn');return false;" xparam="odds_text">2.81</a></td><td class="center info-value">9</td></tr><tr class=" deactivate" xeid="CG1D1dw0"><td class="table-time datet t1374285600-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/chicago-bulls-dallas-mavericks-CG1D1dw0/"><span class="bold">Chicago Bulls</span> - Dallas Mavericks</a></td><td class="center bold table-odds table-score">94:87</td><td class="result-ok odds-nowrp" xoid="E-1l9r1x2rrhkx0x3a2kk" xodd="azefazto"><a href="" onclick="globals.ch.togle(this , 'E-1l9r1x2rrhkx0x3a2kk');return false;" xparam="odds_text">1.46</a></td><td class="odds-nowrp" xoid="E-1l9r1x2rrhkx0x3a2kl" xodd="xz9fxzpa"><a href="" onclick="globals.ch.togle(this , 'E-1l9r1x2rrhkx0x3a2kl');return false;" xparam="odds_text">2.71</a></td><td class="center info-value">9</td></tr><tr class="odd deactivate" xeid="YP292xOg"><td class="table-time datet t1374280200-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/memphis-grizzlies-denver-nuggets-YP292xOg/"><span class="bold">Memphis Grizzlies</span> - Denver Nuggets</a></td><td class="center bold table-odds table-score">91:84</td><td class="result-ok odds-nowrp" xoid="E-1l9r0x2rrhkx0x3a2ki" xodd="az8fazpx"><a href="" onclick="globals.ch.togle(this , 'E-1l9r0x2rrhkx0x3a2ki');return false;" xparam="odds_text">1.72</a></td><td class="odds-nowrp" xoid="E-1l9r0x2rrhkx0x3a2kj" xodd="xzxfxzaa"><a href="" onclick="globals.ch.togle(this , 'E-1l9r0x2rrhkx0x3a2kj');return false;" xparam="odds_text">2.11</a></td><td class="center info-value">9</td></tr><tr class=" deactivate" xeid="j1D43I8m"><td class="table-time datet t1374278400-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/milwaukee-bucks-san-antonio-spurs-j1D43I8m/">Milwaukee Bucks - <span class="bold">San Antonio Spurs</span></a></td><td class="center bold table-odds table-score">80:90</td><td class="odds-nowrp" xoid="E-1l9qvx2rrhkx0x3a2kg" xodd="xz08fx"><a href="" onclick="globals.ch.togle(this , 'E-1l9qvx2rrhkx0x3a2kg');return false;" xparam="odds_text">2.00</a></td><td class="result-ok odds-nowrp" xoid="E-1l9qvx2rrhkx0x3a2kh" xodd="az8efaz8"><a href="" onclick="globals.ch.togle(this , 'E-1l9qvx2rrhkx0x3a2kh');return false;" xparam="odds_text">1.80</a></td><td class="center info-value">9</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374273000-2-0-0-1">19 Jul 2013</span> - Losers Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="hGG1F3po"><td class="table-time datet t1374273000-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/new-orleans-pelicans-washington-wizards-hGG1F3po/">New Orleans Pelicans - <span class="bold">Washington Wizards</span></a></td><td class="center bold table-odds table-score">77:78</td><td class="odds-nowrp" xoid="E-1l9ndx2rrhkx0x3a2dc" xodd="aztofaztx"><a href="" onclick="globals.ch.togle(this , 'E-1l9ndx2rrhkx0x3a2dc');return false;" xparam="odds_text">1.42</a></td><td class="result-ok odds-nowrp" xoid="E-1l9ndx2rrhkx0x3a2dd" xodd="xz9efxz88"><a href="" onclick="globals.ch.togle(this , 'E-1l9ndx2rrhkx0x3a2dd');return false;" xparam="odds_text">2.88</a></td><td class="center info-value">9</td></tr><tr class=" deactivate" xeid="GfPZJqxU"><td class="table-time datet t1374271200-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/atlanta-hawks-sacramento-kings-GfPZJqxU/">Atlanta Hawks - <span class="bold">Sacramento Kings</span></a></td><td class="center bold table-odds table-score">87:93</td><td class="odds-nowrp" xoid="E-1l9ncx2rrhkx0x3a2da" xodd="azcofazcx"><a href="" onclick="globals.ch.togle(this , 'E-1l9ncx2rrhkx0x3a2da');return false;" xparam="odds_text">1.32</a></td><td class="result-ok odds-nowrp" xoid="E-1l9ncx2rrhkx0x3a2db" xodd="czofczc8"><a href="" onclick="globals.ch.togle(this , 'E-1l9ncx2rrhkx0x3a2db');return false;" xparam="odds_text">3.38</a></td><td class="center info-value">9</td></tr><tr class="odd deactivate" xeid="YVZUKPMN"><td class="table-time datet t1374264000-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/new-york-knicks-los-angeles-clippers-YVZUKPMN/"><span class="bold">New York Knicks</span> - Los Angeles Clippers</a></td><td class="center bold table-odds table-score">91:80</td><td class="result-ok odds-nowrp" xoid="E-1l9nbx2rrhkx0x3a2d8" xodd="xzofxztt"><a href="" onclick="globals.ch.togle(this , 'E-1l9nbx2rrhkx0x3a2d8');return false;" xparam="odds_text">2.44</a></td><td class="odds-nowrp" xoid="E-1l9nbx2rrhkx0x3a2d9" xodd="azoafazep"><a href="" onclick="globals.ch.togle(this , 'E-1l9nbx2rrhkx0x3a2d9');return false;" xparam="odds_text">1.57</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374201000-2-0-0-1">19 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="p44Y17af"><td class="table-time datet t1374201000-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/golden-state-warriors-dallas-mavericks-p44Y17af/"><span class="bold">Golden State Warriors</span> - Dallas Mavericks</a></td><td class="center bold table-odds table-score">79:76</td><td class="result-ok odds-nowrp" xoid="E-1l4lnx2rrhkx0x39o8a" xodd="aztefazt"><a href="" onclick="globals.ch.togle(this , 'E-1l4lnx2rrhkx0x39o8a');return false;" xparam="odds_text">1.40</a></td><td class="odds-nowrp" xoid="E-1l4lnx2rrhkx0x39o8b" xodd="czxfxz9t"><a href="" onclick="globals.ch.togle(this , 'E-1l4lnx2rrhkx0x39o8b');return false;" xparam="odds_text">2.94</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="Ic0M9nvk"><td class="table-time datet t1374199200-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/chicago-bulls-miami-heat-Ic0M9nvk/">Chicago Bulls - <span class="bold">Miami Heat</span></a></td><td class="center bold table-odds table-score">62:68</td><td class="odds-nowrp" xoid="E-1l4hcx2rrhkx0x39nvd" xodd="az8pfazpo"><a href="" onclick="globals.ch.togle(this , 'E-1l4hcx2rrhkx0x39nvd');return false;" xparam="odds_text">1.76</a></td><td class="result-ok odds-nowrp" xoid="E-1l4hcx2rrhkx0x39nvc" xodd="xzxfxz0o"><a href="" onclick="globals.ch.togle(this , 'E-1l4hcx2rrhkx0x39nvc');return false;" xparam="odds_text">2.06</a></td><td class="center info-value">9</td></tr><tr class="odd deactivate" xeid="SCXJ1knS"><td class="table-time datet t1374193800-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/nba-d-league-minnesota-timberwolves-SCXJ1knS/"><span class="bold">NBA D-League</span> - Minnesota Timberwolves</a></td><td class="center bold table-odds table-score">83:75</td><td class="result-ok odds-nowrp" xoid="E-1l4h1x2rrhkx0x39nul" xodd="az8fazp8"><a href="" onclick="globals.ch.togle(this , 'E-1l4h1x2rrhkx0x39nul');return false;" xparam="odds_text">1.78</a></td><td class="odds-nowrp" xoid="E-1l4h1x2rrhkx0x39nuk" xodd="xz0tfxz0a"><a href="" onclick="globals.ch.togle(this , 'E-1l4h1x2rrhkx0x39nuk');return false;" xparam="odds_text">2.01</a></td><td class="center info-value">5</td></tr><tr class=" deactivate" xeid="SCgkHUoF"><td class="table-time datet t1374192000-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/phoenix-suns-portland-trail-blazers-SCgkHUoF/"><span class="bold">Phoenix Suns</span> - Portland Trail Blazers</a></td><td class="center bold table-odds table-score">92:84</td><td class="result-ok odds-nowrp" xoid="E-1l4h8x2rrhkx0x39nv2" xodd="azt8faztx"><a href="" onclick="globals.ch.togle(this , 'E-1l4h8x2rrhkx0x39nv2');return false;" xparam="odds_text">1.42</a></td><td class="odds-nowrp" xoid="E-1l4h8x2rrhkx0x39nv3" xodd="czxfxz88"><a href="" onclick="globals.ch.togle(this , 'E-1l4h8x2rrhkx0x39nv3');return false;" xparam="odds_text">2.88</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374186600-2-0-0-1">18 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="4YbCrAuj"><td class="table-time datet t1374186600-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/charlotte-hornets-memphis-grizzlies-4YbCrAuj/"><span class="bold">Charlotte Hornets</span> - Memphis Grizzlies</a></td><td class="center bold table-odds table-score">92:84</td><td class="result-ok odds-nowrp" xoid="E-1l4gqx2rrhkx0x39nu6" xodd="azefaztt"><a href="" onclick="globals.ch.togle(this , 'E-1l4gqx2rrhkx0x39nu6');return false;" xparam="odds_text">1.44</a></td><td class="odds-nowrp" xoid="E-1l4gqx2rrhkx0x39nu7" xodd="cfxzp8"><a href="" onclick="globals.ch.togle(this , 'E-1l4gqx2rrhkx0x39nu7');return false;" xparam="odds_text">2.78</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="x671maRH"><td class="table-time datet t1374184800-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/toronto-raptors-denver-nuggets-x671maRH/"><span class="bold">Toronto Raptors</span> - Denver Nuggets</a></td><td class="center bold table-odds table-score">95:78</td><td class="result-ok odds-nowrp" xoid="E-1l4gfx2rrhkx0x39nt5" xodd="aztpfazt"><a href="" onclick="globals.ch.togle(this , 'E-1l4gfx2rrhkx0x39nt5');return false;" xparam="odds_text">1.40</a></td><td class="odds-nowrp" xoid="E-1l4gfx2rrhkx0x39nt4" xodd="czxfxz99"><a href="" onclick="globals.ch.togle(this , 'E-1l4gfx2rrhkx0x39nt4');return false;" xparam="odds_text">2.99</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="x0n9wf7Q"><td class="table-time datet t1374179400-1-1-0-0 ">20:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/los-angeles-lakers-milwaukee-bucks-x0n9wf7Q/"><span class="bold">Los Angeles Lakers</span> - Milwaukee Bucks</a></td><td class="center bold table-odds table-score">72:68</td><td class="result-ok odds-nowrp" xoid="E-1l1a4x2rrhkx0x39hee" xodd="az98faz9x"><a href="" onclick="globals.ch.togle(this , 'E-1l1a4x2rrhkx0x39hee');return false;" xparam="odds_text">1.92</a></td><td class="odds-nowrp" xoid="E-1l1a4x2rrhkx0x39hef" xodd="az99faz88"><a href="" onclick="globals.ch.togle(this , 'E-1l1a4x2rrhkx0x39hef');return false;" xparam="odds_text">1.88</a></td><td class="center info-value">7</td></tr><tr class=" deactivate" xeid="ChwyZDFs"><td class="table-time datet t1374177600-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/cleveland-cavaliers-san-antonio-spurs-ChwyZDFs/"><span class="bold">Cleveland Cavaliers</span> - San Antonio Spurs</a></td><td class="center bold table-odds table-score">72:66</td><td class="result-ok odds-nowrp" xoid="E-1l1a5x2rrhkx0x39heg" xodd="xzaefaz99"><a href="" onclick="globals.ch.togle(this , 'E-1l1a5x2rrhkx0x39heg');return false;" xparam="odds_text">1.99</a></td><td class="odds-nowrp" xoid="E-1l1a5x2rrhkx0x39heh" xodd="az9xfaz8c"><a href="" onclick="globals.ch.togle(this , 'E-1l1a5x2rrhkx0x39heh');return false;" xparam="odds_text">1.83</a></td><td class="center info-value">7</td></tr><tr class="odd deactivate" xeid="6FxuYXUm"><td class="table-time datet t1374114600-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/dallas-mavericks-los-angeles-clippers-6FxuYXUm/"><span class="bold">Dallas Mavericks</span> - Los Angeles Clippers</a></td><td class="center bold table-odds table-score">95:89</td><td class="result-ok odds-nowrp" xoid="E-1l1a6x2rrhkx0x39hei" xodd="az9xfaz88"><a href="" onclick="globals.ch.togle(this , 'E-1l1a6x2rrhkx0x39hei');return false;" xparam="odds_text">1.88</a></td><td class="odds-nowrp" xoid="E-1l1a6x2rrhkx0x39hej" xodd="xfaz9a"><a href="" onclick="globals.ch.togle(this , 'E-1l1a6x2rrhkx0x39hej');return false;" xparam="odds_text">1.91</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="lbYaT9qJ"><td class="table-time datet t1374112800-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/new-york-knicks-miami-heat-lbYaT9qJ/">New York Knicks - <span class="bold">Miami Heat</span></a></td><td class="center bold table-odds table-score">66:113</td><td class="odds-nowrp" xoid="E-1l1abx2rrhkx0x39hes" xodd="az8fazo9"><a href="" onclick="globals.ch.togle(this , 'E-1l1abx2rrhkx0x39hes');return false;" xparam="odds_text">1.69</a></td><td class="result-ok odds-nowrp" xoid="E-1l1abx2rrhkx0x39het" xodd="xzcefxzao"><a href="" onclick="globals.ch.togle(this , 'E-1l1abx2rrhkx0x39het');return false;" xparam="odds_text">2.16</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="tYUiVVE6"><td class="table-time datet t1374107400-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/portland-trail-blazers-atlanta-hawks-tYUiVVE6/"><span class="bold">Portland Trail Blazers</span> - Atlanta Hawks</a></td><td class="center bold table-odds table-score">70:69 OT</td><td class="result-ok odds-nowrp" xoid="E-1l1a9x2rrhkx0x39heo" xodd="xzxefxzx"><a href="" onclick="globals.ch.togle(this , 'E-1l1a9x2rrhkx0x39heo');return false;" xparam="odds_text">2.20</a></td><td class="odds-nowrp" xoid="E-1l1a9x2rrhkx0x39hep" xodd="azpafazoo"><a href="" onclick="globals.ch.togle(this , 'E-1l1a9x2rrhkx0x39hep');return false;" xparam="odds_text">1.66</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="2sWmWBa0"><td class="table-time datet t1374105600-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/minnesota-timberwolves-sacramento-kings-2sWmWBa0/"><span class="bold">Minnesota Timberwolves</span> - Sacramento Kings</a></td><td class="center bold table-odds table-score">92:54</td><td class="result-ok odds-nowrp" xoid="E-1l1a8x2rrhkx0x39hem" xodd="azofazet"><a href="" onclick="globals.ch.togle(this , 'E-1l1a8x2rrhkx0x39hem');return false;" xparam="odds_text">1.54</a></td><td class="odds-nowrp" xoid="E-1l1a8x2rrhkx0x39hen" xodd="xzocfxzt8"><a href="" onclick="globals.ch.togle(this , 'E-1l1a8x2rrhkx0x39hen');return false;" xparam="odds_text">2.48</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374100200-2-0-0-1">17 Jul 2013</span> - Play Offs</th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="p6yqXipf"><td class="table-time datet t1374100200-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/memphis-grizzlies-washington-wizards-p6yqXipf/"><span class="bold">Memphis Grizzlies</span> - Washington Wizards</a></td><td class="center bold table-odds table-score">90:83</td><td class="result-ok odds-nowrp" xoid="E-1l1a7x2rrhkx0x39hek" xodd="czxfcz09"><a href="" onclick="globals.ch.togle(this , 'E-1l1a7x2rrhkx0x39hek');return false;" xparam="odds_text">3.09</a></td><td class="odds-nowrp" xoid="E-1l1a7x2rrhkx0x39hel" xodd="aztafazc9"><a href="" onclick="globals.ch.togle(this , 'E-1l1a7x2rrhkx0x39hel');return false;" xparam="odds_text">1.39</a></td><td class="center info-value">6</td></tr><tr class=" deactivate" xeid="zeUeUkUC"><td class="table-time datet t1374098400-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/new-orleans-pelicans-denver-nuggets-zeUeUkUC/">New Orleans Pelicans - <span class="bold">Denver Nuggets</span></a></td><td class="center bold table-odds table-score">82:87</td><td class="odds-nowrp" xoid="E-1l1aax2rrhkx0x39heq" xodd="aztfazco"><a href="" onclick="globals.ch.togle(this , 'E-1l1aax2rrhkx0x39heq');return false;" xparam="odds_text">1.36</a></td><td class="result-ok odds-nowrp" xoid="E-1l1aax2rrhkx0x39her" xodd="cztfczxc"><a href="" onclick="globals.ch.togle(this , 'E-1l1aax2rrhkx0x39her');return false;" xparam="odds_text">3.23</a></td><td class="center info-value">6</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374028200-2-0-0-1">17 Jul 2013</span></th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="MLktWRTr"><td class="table-time datet t1374028200-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/nba-d-league-dallas-mavericks-MLktWRTr/"><span class="bold">NBA D-League</span> - Dallas Mavericks</a></td><td class="center bold table-odds table-score">82:75</td><td class="result-ok odds-nowrp" xoid="E-1k9j5x2rrhkx0x381mb" xodd="azoafazeo"><a href="" onclick="globals.ch.togle(this , 'E-1k9j5x2rrhkx0x381mb');return false;" xparam="odds_text">1.56</a></td><td class="odds-nowrp" xoid="E-1k9j5x2rrhkx0x381mc" xodd="xzofxzte"><a href="" onclick="globals.ch.togle(this , 'E-1k9j5x2rrhkx0x381mc');return false;" xparam="odds_text">2.45</a></td><td class="center info-value">6</td></tr><tr class=" deactivate" xeid="lUY3kGU3"><td class="table-time datet t1374026400-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/washington-wizards-denver-nuggets-lUY3kGU3/"><span class="bold">Washington Wizards</span> - Denver Nuggets</a></td><td class="center bold table-odds table-score">97:69</td><td class="result-ok odds-nowrp" xoid="E-1k9j2x2rrhkx0x381m5" xodd="xzc8fxzap"><a href="" onclick="globals.ch.togle(this , 'E-1k9j2x2rrhkx0x381m5');return false;" xparam="odds_text">2.17</a></td><td class="odds-nowrp" xoid="E-1k9j2x2rrhkx0x381m6" xodd="az8fazo8"><a href="" onclick="globals.ch.togle(this , 'E-1k9j2x2rrhkx0x381m6');return false;" xparam="odds_text">1.68</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="AqNCmfaG"><td class="table-time datet t1374021000-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/memphis-grizzlies-phoenix-suns-AqNCmfaG/">Memphis Grizzlies - <span class="bold">Phoenix Suns</span></a></td><td class="center bold table-odds table-score">88:100</td><td class="odds-nowrp" xoid="E-1k9j4x2rrhkx0x381m9" xodd="xzopfxzea"><a href="" onclick="globals.ch.togle(this , 'E-1k9j4x2rrhkx0x381m9');return false;" xparam="odds_text">2.51</a></td><td class="result-ok odds-nowrp" xoid="E-1k9j4x2rrhkx0x381ma" xodd="azofazec"><a href="" onclick="globals.ch.togle(this , 'E-1k9j4x2rrhkx0x381ma');return false;" xparam="odds_text">1.53</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="t4ZajdFc"><td class="table-time datet t1374019200-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/portland-trail-blazers-chicago-bulls-t4ZajdFc/">Portland Trail Blazers - <span class="bold">Chicago Bulls</span></a></td><td class="center bold table-odds table-score">78:80 OT</td><td class="odds-nowrp" xoid="E-1k9j1x2rrhkx0x381m3" xodd="xzetfxzt"><a href="" onclick="globals.ch.togle(this , 'E-1k9j1x2rrhkx0x381m3');return false;" xparam="odds_text">2.40</a></td><td class="result-ok odds-nowrp" xoid="E-1k9j1x2rrhkx0x381m4" xodd="azocfazep"><a href="" onclick="globals.ch.togle(this , 'E-1k9j1x2rrhkx0x381m4');return false;" xparam="odds_text">1.57</a></td><td class="center info-value">8</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1374013800-2-0-0-1">16 Jul 2013</span></th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="SKX7lzpA"><td class="table-time datet t1374013800-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/milwaukee-bucks-golden-state-warriors-SKX7lzpA/">Milwaukee Bucks - <span class="bold">Golden State Warriors</span></a></td><td class="center bold table-odds table-score">72:84</td><td class="odds-nowrp" xoid="E-1k9j3x2rrhkx0x381m7" xodd="az8fazpp"><a href="" onclick="globals.ch.togle(this , 'E-1k9j3x2rrhkx0x381m7');return false;" xparam="odds_text">1.77</a></td><td class="result-ok odds-nowrp" xoid="E-1k9j3x2rrhkx0x381m8" xodd="xzxfxz0t"><a href="" onclick="globals.ch.togle(this , 'E-1k9j3x2rrhkx0x381m8');return false;" xparam="odds_text">2.04</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="fZmlU5be"><td class="table-time datet t1374012000-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/toronto-raptors-sacramento-kings-fZmlU5be/"><span class="bold">Toronto Raptors</span> - Sacramento Kings</a></td><td class="center bold table-odds table-score">81:70</td><td class="result-ok odds-nowrp" xoid="E-1k9j7x2rrhkx0x381mf" xodd="azeefazto"><a href="" onclick="globals.ch.togle(this , 'E-1k9j7x2rrhkx0x381mf');return false;" xparam="odds_text">1.46</a></td><td class="odds-nowrp" xoid="E-1k9j7x2rrhkx0x381mg" xodd="cfxzp"><a href="" onclick="globals.ch.togle(this , 'E-1k9j7x2rrhkx0x381mg');return false;" xparam="odds_text">2.70</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="2Dzdix0i"><td class="table-time datet t1374004800-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/miami-heat-minnesota-timberwolves-2Dzdix0i/">Miami Heat - <span class="bold">Minnesota Timberwolves</span></a></td><td class="center bold table-odds table-score">71:80</td><td class="odds-nowrp" xoid="E-1k9j0x2rrhkx0x381m1" xodd="azoxfazeo"><a href="" onclick="globals.ch.togle(this , 'E-1k9j0x2rrhkx0x381m1');return false;" xparam="odds_text">1.56</a></td><td class="result-ok odds-nowrp" xoid="E-1k9j0x2rrhkx0x381m2" xodd="cfxzex"><a href="" onclick="globals.ch.togle(this , 'E-1k9j0x2rrhkx0x381m2');return false;" xparam="odds_text">2.52</a></td><td class="center info-value">6</td></tr><tr class=" deactivate" xeid="08dDShNj"><td class="table-time datet t1373941800-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/denver-nuggets-chicago-bulls-08dDShNj/">Denver Nuggets - <span class="bold">Chicago Bulls</span></a></td><td class="center bold table-odds table-score">81:93</td><td class="odds-nowrp" xoid="E-1k9ivx2rrhkx0x381lv" xodd="xzxefxza9"><a href="" onclick="globals.ch.togle(this , 'E-1k9ivx2rrhkx0x381lv');return false;" xparam="odds_text">2.19</a></td><td class="result-ok odds-nowrp" xoid="E-1k9ivx2rrhkx0x381m0" xodd="azpefazop"><a href="" onclick="globals.ch.togle(this , 'E-1k9ivx2rrhkx0x381m0');return false;" xparam="odds_text">1.67</a></td><td class="center info-value">9</td></tr><tr class="odd deactivate" xeid="jZ6wZfpN"><td class="table-time datet t1373940000-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/atlanta-hawks-san-antonio-spurs-jZ6wZfpN/">Atlanta Hawks - <span class="bold">San Antonio Spurs</span></a></td><td class="center bold table-odds table-score">87:96</td><td class="odds-nowrp" xoid="E-1k9isx2rrhkx0x381lp" xodd="az8cfazpt"><a href="" onclick="globals.ch.togle(this , 'E-1k9isx2rrhkx0x381lp');return false;" xparam="odds_text">1.74</a></td><td class="result-ok odds-nowrp" xoid="E-1k9isx2rrhkx0x381lq" xodd="xzaofxz08"><a href="" onclick="globals.ch.togle(this , 'E-1k9isx2rrhkx0x381lq');return false;" xparam="odds_text">2.08</a></td><td class="center info-value">9</td></tr><tr class=" deactivate" xeid="n5h9TY7p"><td class="table-time datet t1373934600-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/golden-state-warriors-sacramento-kings-n5h9TY7p/"><span class="bold">Golden State Warriors</span> - Sacramento Kings</a></td><td class="center bold table-odds table-score">80:66</td><td class="result-ok odds-nowrp" xoid="E-1k9iux2rrhkx0x381lt" xodd="azp8fazpt"><a href="" onclick="globals.ch.togle(this , 'E-1k9iux2rrhkx0x381lt');return false;" xparam="odds_text">1.74</a></td><td class="odds-nowrp" xoid="E-1k9iux2rrhkx0x381lu" xodd="xzxxfxz09"><a href="" onclick="globals.ch.togle(this , 'E-1k9iux2rrhkx0x381lu');return false;" xparam="odds_text">2.09</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="YcCYZzVG"><td class="table-time datet t1373932800-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/los-angeles-lakers-los-angeles-clippers-YcCYZzVG/"><span class="bold">Los Angeles Lakers</span> - Los Angeles Clippers</a></td><td class="center bold table-odds table-score">77:65</td><td class="result-ok odds-nowrp" xoid="E-1k9irx2rrhkx0x381ln" xodd="az8efaz8"><a href="" onclick="globals.ch.togle(this , 'E-1k9irx2rrhkx0x381ln');return false;" xparam="odds_text">1.80</a></td><td class="odds-nowrp" xoid="E-1k9irx2rrhkx0x381lo" xodd="xz0tfx"><a href="" onclick="globals.ch.togle(this , 'E-1k9irx2rrhkx0x381lo');return false;" xparam="odds_text">2.00</a></td><td class="center info-value">9</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1373927400-2-0-0-1">15 Jul 2013</span></th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="UP5sYEaT"><td class="table-time datet t1373927400-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/phoenix-suns-minnesota-timberwolves-UP5sYEaT/"><span class="bold">Phoenix Suns</span> - Minnesota Timberwolves</a></td><td class="center bold table-odds table-score">91:89</td><td class="result-ok odds-nowrp" xoid="E-1k9itx2rrhkx0x381lr" xodd="az8fazo8"><a href="" onclick="globals.ch.togle(this , 'E-1k9itx2rrhkx0x381lr');return false;" xparam="odds_text">1.68</a></td><td class="odds-nowrp" xoid="E-1k9itx2rrhkx0x381ls" xodd="xzcefxza8"><a href="" onclick="globals.ch.togle(this , 'E-1k9itx2rrhkx0x381ls');return false;" xparam="odds_text">2.18</a></td><td class="center info-value">7</td></tr><tr class=" deactivate" xeid="f7DUzHFA"><td class="table-time datet t1373925600-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/new-orleans-pelicans-cleveland-cavaliers-f7DUzHFA/"><span class="bold">New Orleans Pelicans</span> - Cleveland Cavaliers</a></td><td class="center bold table-odds table-score">66:62</td><td class="result-ok odds-nowrp" xoid="E-1k9iqx2rrhkx0x381ll" xodd="xz9ofxzp8"><a href="" onclick="globals.ch.togle(this , 'E-1k9iqx2rrhkx0x381ll');return false;" xparam="odds_text">2.78</a></td><td class="odds-nowrp" xoid="E-1k9iqx2rrhkx0x381lm" xodd="aztefaztt"><a href="" onclick="globals.ch.togle(this , 'E-1k9iqx2rrhkx0x381lm');return false;" xparam="odds_text">1.44</a></td><td class="center info-value">8</td></tr><tr class="odd deactivate" xeid="0pEQyc04"><td class="table-time datet t1373918400-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/charlotte-hornets-new-york-knicks-0pEQyc04/"><span class="bold">Charlotte Hornets</span> - New York Knicks</a></td><td class="center bold table-odds table-score">84:71</td><td class="result-ok odds-nowrp" xoid="E-1k9ipx2rrhkx0x381lj" xodd="azexfazto"><a href="" onclick="globals.ch.togle(this , 'E-1k9ipx2rrhkx0x381lj');return false;" xparam="odds_text">1.46</a></td><td class="odds-nowrp" xoid="E-1k9ipx2rrhkx0x381lk" xodd="xz9fxzpa"><a href="" onclick="globals.ch.togle(this , 'E-1k9ipx2rrhkx0x381lk');return false;" xparam="odds_text">2.71</a></td><td class="center info-value">8</td></tr><tr class=" deactivate" xeid="GrkpVoqk"><td class="table-time datet t1373855400-1-1-0-0 ">02:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/toronto-raptors-san-antonio-spurs-GrkpVoqk/"><span class="bold">Toronto Raptors</span> - San Antonio Spurs</a></td><td class="center bold table-odds table-score">82:76</td><td class="result-ok odds-nowrp" xoid="E-1k9j6x2rrhkx0x381md" xodd="az9afaz8t"><a href="" onclick="globals.ch.togle(this , 'E-1k9j6x2rrhkx0x381md');return false;" xparam="odds_text">1.84</a></td><td class="odds-nowrp" xoid="E-1k9j6x2rrhkx0x381me" xodd="xfaz9o"><a href="" onclick="globals.ch.togle(this , 'E-1k9j6x2rrhkx0x381me');return false;" xparam="odds_text">1.96</a></td><td class="center info-value">5</td></tr><tr class="odd deactivate" xeid="vuTVFFwo"><td class="table-time datet t1373853600-1-1-0-0 ">02:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/miami-heat-atlanta-hawks-vuTVFFwo/">Miami Heat - <span class="bold">Atlanta Hawks</span></a></td><td class="center bold table-odds table-score">71:75</td><td class="odds-nowrp" xoid="E-1k9ilx2rrhkx0x381lb" xodd="azpfazop"><a href="" onclick="globals.ch.togle(this , 'E-1k9ilx2rrhkx0x381lb');return false;" xparam="odds_text">1.67</a></td><td class="result-ok odds-nowrp" xoid="E-1k9ilx2rrhkx0x381lc" xodd="xzcefxzxc"><a href="" onclick="globals.ch.togle(this , 'E-1k9ilx2rrhkx0x381lc');return false;" xparam="odds_text">2.23</a></td><td class="center info-value">6</td></tr><tr class=" deactivate" xeid="lAAMxwob"><td class="table-time datet t1373848200-1-1-0-0 ">00:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/milwaukee-bucks-new-orleans-pelicans-lAAMxwob/"><span class="bold">Milwaukee Bucks</span> - New Orleans Pelicans</a></td><td class="center bold table-odds table-score">69:61</td><td class="result-ok odds-nowrp" xoid="E-1k9iox2rrhkx0x381lh" xodd="az8xfazpp"><a href="" onclick="globals.ch.togle(this , 'E-1k9iox2rrhkx0x381lh');return false;" xparam="odds_text">1.77</a></td><td class="odds-nowrp" xoid="E-1k9iox2rrhkx0x381li" xodd="xzafxz0o"><a href="" onclick="globals.ch.togle(this , 'E-1k9iox2rrhkx0x381li');return false;" xparam="odds_text">2.06</a></td><td class="center info-value">5</td></tr><tr class="odd deactivate" xeid="xWt4KeVT"><td class="table-time datet t1373846400-1-1-0-0 ">00:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/memphis-grizzlies-cleveland-cavaliers-xWt4KeVT/">Memphis Grizzlies - <span class="bold">Cleveland Cavaliers</span></a></td><td class="center bold table-odds table-score">58:69</td><td class="odds-nowrp" xoid="E-1k9ikx2rrhkx0x381l9" xodd="xzx9fxza9"><a href="" onclick="globals.ch.togle(this , 'E-1k9ikx2rrhkx0x381l9');return false;" xparam="odds_text">2.19</a></td><td class="result-ok odds-nowrp" xoid="E-1k9ikx2rrhkx0x381la" xodd="azpcfazp"><a href="" onclick="globals.ch.togle(this , 'E-1k9ikx2rrhkx0x381la');return false;" xparam="odds_text">1.70</a></td><td class="center info-value">6</td></tr><tr class="center nob-border"><th class="first2 tl" colspan="4"><span class="datet t1373841000-2-0-0-1">14 Jul 2013</span></th><th>1</th><th>2</th><th xparam="Number of available bookmakers odds~2">B's</th></tr><tr class="table-dummyrow"><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr class="odd deactivate" xeid="6oLHwJVi"><td class="table-time datet t1373841000-1-1-0-0 ">22:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/portland-trail-blazers-los-angeles-lakers-6oLHwJVi/">Portland Trail Blazers - <span class="bold">Los Angeles Lakers</span></a></td><td class="center bold table-odds table-score">63:81</td><td class="odds-nowrp" xoid="E-1k9inx2rrhkx0x381lf" xodd="az8efaz8"><a href="" onclick="globals.ch.togle(this , 'E-1k9inx2rrhkx0x381lf');return false;" xparam="odds_text">1.80</a></td><td class="result-ok odds-nowrp" xoid="E-1k9inx2rrhkx0x381lg" xodd="xzaefxz0x"><a href="" onclick="globals.ch.togle(this , 'E-1k9inx2rrhkx0x381lg');return false;" xparam="odds_text">2.02</a></td><td class="center info-value">5</td></tr><tr class=" deactivate" xeid="f7iaLyGN"><td class="table-time datet t1373839200-1-1-0-0 ">22:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/dallas-mavericks-charlotte-hornets-f7iaLyGN/">Dallas Mavericks - <span class="bold">Charlotte Hornets</span></a></td><td class="center bold table-odds table-score">80:86</td><td class="odds-nowrp" xoid="E-1k9ijx2rrhkx0x381l8" xodd="az8ofaz8x"><a href="" onclick="globals.ch.togle(this , 'E-1k9ijx2rrhkx0x381l8');return false;" xparam="odds_text">1.82</a></td><td class="result-ok odds-nowrp" xoid="E-1k9ijx2rrhkx0x381l7" xodd="xz0tfaz98"><a href="" onclick="globals.ch.togle(this , 'E-1k9ijx2rrhkx0x381l7');return false;" xparam="odds_text">1.98</a></td><td class="center info-value">6</td></tr><tr class="odd deactivate" xeid="SfMDvaGo"><td class="table-time datet t1373833800-1-1-0-0 ">20:30</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/nba-d-league-los-angeles-clippers-SfMDvaGo/"><span class="bold">NBA D-League</span> - Los Angeles Clippers</a></td><td class="center bold table-odds table-score">81:77</td><td class="result-ok odds-nowrp" xoid="E-1k9imx2rrhkx0x381ld" xodd="azpafazpa"><a href="" onclick="globals.ch.togle(this , 'E-1k9imx2rrhkx0x381ld');return false;" xparam="odds_text">1.71</a></td><td class="odds-nowrp" xoid="E-1k9imx2rrhkx0x381le" xodd="xzxfxzx"><a href="" onclick="globals.ch.togle(this , 'E-1k9imx2rrhkx0x381le');return false;" xparam="odds_text">2.20</a></td><td class="center info-value">2</td></tr><tr class=" deactivate" xeid="t4meMH0H"><td class="table-time datet t1373832000-1-1-0-0 ">20:00</td><td class="name table-participant" colspan="2"><a href="/basketball/usa/nba-las-vegas-summer-league-2013/washington-wizards-new-york-knicks-t4meMH0H/">Washington Wizards - <span class="bold">New York Knicks</span></a></td><td class="center bold table-odds table-score">69:82</td><td class="odds-nowrp" xoid="E-1k9iix2rrhkx0x381l5" xodd="xfaz9p"><a href="" onclick="globals.ch.togle(this , 'E-1k9iix2rrhkx0x381l5');return false;" xparam="odds_text">1.97</a></td><td class="result-ok odds-nowrp" xoid="E-1k9iix2rrhkx0x381l6" xodd="az9afaz8t"><a href="" onclick="globals.ch.togle(this , 'E-1k9iix2rrhkx0x381l6');return false;" xparam="odds_text">1.84</a></td><td class="center info-value">6</td></tr></tbody></table><div id="pagination"><a href="#/" x-page="1"><span class="arrow">|«</span></a><a href="#/" x-page="1"><span class="arrow">«</span></a><span class="active-page">1</span><a href="#/page/2/" x-page="2"><span>2</span></a><a href="#/page/2/" x-page="2"><span class="arrow">»</span></a><a href="#/page/2/" x-page="2"><span class="arrow">»|</span></a></div></div><div id="event-wait-msg-main" style="display: none;"><div id="event-wait-msg"></div></div><p id="bookmarks-link"><a href="#" xbid="16153" xtext="NBA Las Vegas Summer League 2013">Add "NBA Las Vegas Summer League 2013" to My Leagues</a></p><div id="share-buttons-detail"><span class="share-button facebook" onclick="share_button_click('facebook');" title="Share on Facebook"></span><span class="share-button twitter" onclick="share_button_click('twitter');" title="Share on Twitter"></span><span class="share-button googleplus last" onclick="share_button_click('googleplus');" title="Share on Google+"></span><span class="cleaner" style="clear:both;"></span></div><div id="bonnus-offers-placeholder"></div><div class="about-text"><div class="cms"><p>Help for Odds Archive page: This page serves to display archive odds / historical odds of NBA Las Vegas Summer League 2013 which is sorted in USA category of OddsPortal odds comparison service. Find out what chances and odds the teams had in historical matches, browse through historical odds archive of previous matches in NBA Las Vegas Summer League 2013. Odds Portal makes evidence of highest or lowest odds, opening and closing odds and average / highest values for NBA Las Vegas Summer League 2013 archive matches.</p></div></div>                    <!--  END PAGE BODY -->
                </div>
                <!-- LEFT MENU -->
                <div id="col-side">
                    <!-- SPORT MENU -->
                        <div id="bookmarks-menu"><div id="my-box2"><div id="my-box2-head" class="head"><div class="head-bottom"><h2><a href="#" onclick="return clickMenu('lmbt');" class="my-leagues-open-button"> </a><a href="#" onclick="return clickMenu('lmbt');">My Leagues</a> <span id="my-leagues-count">(0)</span></h2></div></div><div class="body box"><div id="lmbt" class="hidden"><table class="table-main"></table></div></div><div class="corner-box manage-my-leagues"><div class="spc dark2"><div class="body2"><p class="all"><span class="r"><a href="/manage-my-leagues">Manage My Leagues</a></span> </p></div></div></div></div></div>
    <div class="spacer10"></div>
    <div id="search-box">
        <div class="spc">
            <div class="form">
                <h2><label for="search">Search</label></h2>

                <p>
                    <a id="search-submit" xparam="Search"><span>Search</span></a>
                    <input type="text" class="int-text" name="search-event" id="search" value="team / player" autocomplete="off" />

                </p>
            </div>
        </div>
    </div>
    <div class="spacer10"></div>
    <div class="adsenvelope adstextpad banx-left_menu_1" id="lsadvert-zid-254" style="width:185px;"><div style="height:60px"><div class="adsclick" style="width: 100% !important; height: 100% !important" onclick="window.open('https://ads.livesportmedia.eu/www/delivery/ck.php?oaparams=2__bannerid=32716__zoneid=254', 'banner')"></div><div class="adscontent" id="lsadvert-left_menu_1"><iframe id="lsadvert-zid-254-iframe" name="banx-left_menu_1" frameborder="0" scrolling="no" style="width: 185px; height: 60px;"></iframe></div><div class="adstext"><span>advertisement</span></div></div></div><div id="side-menu"><h2>Sports</h2>
<ul id="sports-menu">

                                    <li class="sport"><div class="sport_name"><a href="/soccer/" onclick="return clickMenu('s_1');" class="siconleft s1">Soccer</a></div>
                                        <div id="s_1" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/soccer/">Today's matches</a></li>
                                                    <li class="country"><span class="f f-popular"> </span><a href="#" onclick="return clickMenu('sub_1_popular');"> <span>Popular</span></a>
                                                        <ul id="sub_1_popular" class="hidden">
                                                
                                                <li id="pt_28319" class="tournament">
                                                    <a href="/soccer/england/premier-league/">Premier League</a>
                                                    <span class="number"> (30)</span>
                                                </li>
                                            
                                                <li id="pt_26394" class="tournament">
                                                    <a href="/soccer/europe/champions-league/">Champions League</a>
                                                    <span class="number"> (26)</span>
                                                </li>
                                            
                                                <li id="pt_26395" class="tournament">
                                                    <a href="/soccer/europe/europa-league/">Europa League</a>
                                                    <span class="number"> (65)</span>
                                                </li>
                                            
                                                <li id="pt_28035" class="tournament">
                                                    <a href="/soccer/france/ligue-1/">Ligue 1</a>
                                                    <span class="number"> (20)</span>
                                                </li>
                                            
                                                <li id="pt_28418" class="tournament">
                                                    <a href="/soccer/germany/bundesliga/">Bundesliga</a>
                                                    <span class="number"> (27)</span>
                                                </li>
                                            
                                                <li id="pt_22894" class="tournament">
                                                    <a href="/soccer/world/world-cup-2018/">World Cup 2018</a>
                                                    <span class="number"> (34)</span>
                                                </li>
                                            
                                                </ul>
                                            </li>
                                        <li class="country"><span class="f f-22"> </span><a href="/soccer/argentina/" onclick="return clickMenu('sub_1_22');"> <span>Argentina</span></a>  <ul id="sub_1_22" class="hidden"><li id="t_26858" class="tournament">
                                            <a href="/soccer/argentina/primera-b-nacional/">Primera B Nacional</a><span class="number"> (11)</span>  </li>
                                    
                                          </ul></li><li class="country"><span class="f f-24"> </span><a href="/soccer/australia/" onclick="return clickMenu('sub_1_24');"> <span>Australia</span></a>  <ul id="sub_1_24" class="hidden"><li id="t_33134" class="tournament">
                                            <a href="/soccer/australia/a-league/">A-League</a><span class="number"> (5)</span>  </li>
                                    <li id="t_30966" class="tournament">
                                            <a href="/soccer/australia/npl-nsw/">NPL NSW</a><span class="number"> (6)</span>  </li>
                                    <li id="t_30963" class="tournament">
                                            <a href="/soccer/australia/npl-victoria/">NPL Victoria</a><span class="number"> (6)</span>  </li>
                                    <li id="t_31398" class="tournament">
                                            <a href="/soccer/australia/npl-western-australia/">NPL Western Australia</a><span class="number"> (7)</span>  </li>
                                    <li id="t_30969" class="tournament">
                                            <a href="/soccer/australia/npl-south-australian/">NPL South Australian</a><span class="number"> (6)</span>  </li>
                                    <li id="t_31196" class="tournament">
                                            <a href="/soccer/australia/npl-queensland/">NPL Queensland</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-25"> </span><a href="/soccer/austria/" onclick="return clickMenu('sub_1_25');"> <span>Austria</span></a>  <ul id="sub_1_25" class="hidden"><li id="t_28307" class="tournament">
                                            <a href="/soccer/austria/tipico-bundesliga/">Tipico Bundesliga</a><span class="number"> (5)</span>  </li>
                                    <li id="t_28210" class="tournament">
                                            <a href="/soccer/austria/erste-liga/">Erste Liga</a><span class="number"> (5)</span>  </li>
                                    <li id="t_33080" class="tournament">
                                            <a href="/soccer/austria/ofb-cup/">OFB Cup</a><span class="number"> (32)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-32"> </span><a href="/soccer/belgium/" onclick="return clickMenu('sub_1_32');"> <span>Belgium</span></a>  <ul id="sub_1_32" class="hidden"><li id="t_28370" class="tournament">
                                            <a href="/soccer/belgium/jupiler-league/">Jupiler League</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32592" class="tournament">
                                            <a href="/soccer/belgium/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-39"> </span><a href="/soccer/brazil/" onclick="return clickMenu('sub_1_39');"> <span>Brazil</span></a>  <ul id="sub_1_39" class="hidden"><li id="t_27187" class="tournament">
                                            <a href="/soccer/brazil/serie-a/">Série A</a><span class="number"> (11)</span>  </li>
                                    <li id="t_27188" class="tournament">
                                            <a href="/soccer/brazil/serie-b/">Série B</a><span class="number"> (13)</span>  </li>
                                    <li id="t_33242" class="tournament">
                                            <a href="/soccer/brazil/brasileiro-u20/">Brasileiro U20</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-41"> </span><a href="/soccer/bulgaria/" onclick="return clickMenu('sub_1_41');"> <span>Bulgaria</span></a>  <ul id="sub_1_41" class="hidden"><li id="t_28931" class="tournament">
                                            <a href="/soccer/bulgaria/parva-liga/">Parva Liga</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-46"> </span><a href="/soccer/cameroon/" onclick="return clickMenu('sub_1_46');"> <span>Cameroon</span></a>  <ul id="sub_1_46" class="hidden"><li id="t_31387" class="tournament">
                                            <a href="/soccer/cameroon/elite-one/">Elite One</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-47"> </span><a href="/soccer/canada/" onclick="return clickMenu('sub_1_47');"> <span>Canada</span></a>  <ul id="sub_1_47" class="hidden"><li id="t_32371" class="tournament">
                                            <a href="/soccer/canada/csl/">CSL</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-52"> </span><a href="/soccer/china/" onclick="return clickMenu('sub_1_52');"> <span>China</span></a>  <ul id="sub_1_52" class="hidden"><li id="t_27135" class="tournament">
                                            <a href="/soccer/china/super-league/">Super League</a><span class="number"> (8)</span>  </li>
                                    <li id="t_26986" class="tournament">
                                            <a href="/soccer/china/jia-league/">Jia League</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32021" class="tournament">
                                            <a href="/soccer/china/yi-league/">Yi League</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-53"> </span><a href="/soccer/colombia/" onclick="return clickMenu('sub_1_53');"> <span>Colombia</span></a>  <ul id="sub_1_53" class="hidden"><li id="t_31230" class="tournament">
                                            <a href="/soccer/colombia/liga-aguila/">Liga Aguila</a><span class="number"> (10)</span>  </li>
                                    <li id="t_31234" class="tournament">
                                            <a href="/soccer/colombia/torneo-aguila/">Torneo Aguila</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31675" class="tournament">
                                            <a href="/soccer/colombia/copa-aguila/">Copa Aguila</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-59"> </span><a href="/soccer/croatia/" onclick="return clickMenu('sub_1_59');"> <span>Croatia</span></a>  <ul id="sub_1_59" class="hidden"><li id="t_28759" class="tournament">
                                            <a href="/soccer/croatia/1-hnl/">1. HNL</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-62"> </span><a href="/soccer/czech-republic/" onclick="return clickMenu('sub_1_62');"> <span>Czech Republic</span></a>  <ul id="sub_1_62" class="hidden"><li id="t_28292" class="tournament">
                                            <a href="/soccer/czech-republic/1-liga/">1. Liga</a><span class="number"> (9)</span>  </li>
                                    <li id="t_33062" class="tournament">
                                            <a href="/soccer/czech-republic/mol-cup/">MOL Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-63"> </span><a href="/soccer/denmark/" onclick="return clickMenu('sub_1_63');"> <span>Denmark</span></a>  <ul id="sub_1_63" class="hidden"><li id="t_28333" class="tournament">
                                            <a href="/soccer/denmark/superliga/">Superliga</a><span class="number"> (13)</span>  </li>
                                    <li id="t_30817" class="tournament">
                                            <a href="/soccer/denmark/1st-division/">1st Division</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-69"> </span><a href="/soccer/egypt/" onclick="return clickMenu('sub_1_69');"> <span>Egypt</span></a>  <ul id="sub_1_69" class="hidden"><li id="t_29447" class="tournament">
                                            <a href="/soccer/egypt/premier-league/">Premier League</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30936" class="tournament">
                                            <a href="/soccer/egypt/egypt-cup/">Egypt Cup</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-198"> </span><a href="/soccer/england/" onclick="return clickMenu('sub_1_198');"> <span>England</span></a>  <ul id="sub_1_198" class="hidden"><li id="t_28319" class="tournament">
                                            <a href="/soccer/england/premier-league/">Premier League</a><span class="number"> (30)</span>  </li>
                                    <li id="t_28217" class="tournament">
                                            <a href="/soccer/england/championship/">Championship</a><span class="number"> (24)</span>  </li>
                                    <li id="t_28318" class="tournament">
                                            <a href="/soccer/england/league-one/">League One</a><span class="number"> (12)</span>  </li>
                                    <li id="t_28317" class="tournament">
                                            <a href="/soccer/england/league-two/">League Two</a><span class="number"> (12)</span>  </li>
                                    <li id="t_32904" class="tournament">
                                            <a href="/soccer/england/carabao-cup/">Carabao Cup</a><span class="number"> (35)</span>  </li>
                                    <li id="t_32670" class="tournament">
                                            <a href="/soccer/england/fa-community-shield/">FA Community Shield</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-73"> </span><a href="/soccer/estonia/" onclick="return clickMenu('sub_1_73');"> <span>Estonia</span></a>  <ul id="sub_1_73" class="hidden"><li id="t_31052" class="tournament">
                                            <a href="/soccer/estonia/meistriliiga/">Meistriliiga</a><span class="number"> (4)</span>  </li>
                                    <li id="t_26408" class="tournament">
                                            <a href="/soccer/estonia/esiliiga/">Esiliiga</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-6"> </span><a href="/soccer/europe/" onclick="return clickMenu('sub_1_6');"> <span>Europe</span></a>  <ul id="sub_1_6" class="hidden"><li id="t_26394" class="tournament">
                                            <a href="/soccer/europe/champions-league/">Champions League</a><span class="number"> (26)</span>  </li>
                                    <li id="t_26395" class="tournament">
                                            <a href="/soccer/europe/europa-league/">Europa League</a><span class="number"> (65)</span>  </li>
                                    <li id="t_32683" class="tournament">
                                            <a href="/soccer/europe/uefa-super-cup/">UEFA Super Cup</a><span class="number"> (1)</span>  </li>
                                    <li id="t_28240" class="tournament">
                                            <a href="/soccer/europe/euro-u19/">Euro U19</a><span class="number"> (2)</span>  </li>
                                    <li id="t_32477" class="tournament">
                                            <a href="/soccer/europe/uhren-cup/">Uhren Cup</a><span class="number"> (2)</span>  </li>
                                    <li id="t_8900" class="tournament">
                                            <a href="/soccer/europe/euro-women/">Euro Women</a><span class="number"> (8)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-76"> </span><a href="/soccer/finland/" onclick="return clickMenu('sub_1_76');"> <span>Finland</span></a>  <ul id="sub_1_76" class="hidden"><li id="t_26726" class="tournament">
                                            <a href="/soccer/finland/veikkausliiga/">Veikkausliiga</a><span class="number"> (5)</span>  </li>
                                    <li id="t_26727" class="tournament">
                                            <a href="/soccer/finland/ykkonen/">Ykkonen</a><span class="number"> (5)</span>  </li>
                                    <li id="t_31363" class="tournament">
                                            <a href="/soccer/finland/kakkonen-group-a/">Kakkonen Group A</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31364" class="tournament">
                                            <a href="/soccer/finland/kakkonen-group-b/">Kakkonen Group B</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-77"> </span><a href="/soccer/france/" onclick="return clickMenu('sub_1_77');"> <span>France</span></a>  <ul id="sub_1_77" class="hidden"><li id="t_28035" class="tournament">
                                            <a href="/soccer/france/ligue-1/">Ligue 1</a><span class="number"> (20)</span>  </li>
                                    <li id="t_28036" class="tournament">
                                            <a href="/soccer/france/ligue-2/">Ligue 2</a><span class="number"> (10)</span>  </li>
                                    <li id="t_32605" class="tournament">
                                            <a href="/soccer/france/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-81"> </span><a href="/soccer/germany/" onclick="return clickMenu('sub_1_81');"> <span>Germany</span></a>  <ul id="sub_1_81" class="hidden"><li id="t_28418" class="tournament">
                                            <a href="/soccer/germany/bundesliga/">Bundesliga</a><span class="number"> (27)</span>  </li>
                                    <li id="t_28414" class="tournament">
                                            <a href="/soccer/germany/2-bundesliga/">2. Bundesliga</a><span class="number"> (9)</span>  </li>
                                    <li id="t_28419" class="tournament">
                                            <a href="/soccer/germany/3-liga/">3. Liga</a><span class="number"> (10)</span>  </li>
                                    <li id="t_28345" class="tournament">
                                            <a href="/soccer/germany/regionalliga-bayern/">Regionalliga Bayern</a><span class="number"> (6)</span>  </li>
                                    <li id="t_32817" class="tournament">
                                            <a href="/soccer/germany/dfb-pokal/">DFB Pokal</a><span class="number"> (32)</span>  </li>
                                    <li id="t_32604" class="tournament">
                                            <a href="/soccer/germany/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30841" class="tournament">
                                            <a href="/soccer/germany/telekom-cup-summer/">Telekom Cup - summer</a><span class="number"> (2)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-82"> </span><a href="/soccer/ghana/" onclick="return clickMenu('sub_1_82');"> <span>Ghana</span></a>  <ul id="sub_1_82" class="hidden"><li id="t_31301" class="tournament">
                                            <a href="/soccer/ghana/premier-league/">Premier League</a><span class="number"> (8)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-92"> </span><a href="/soccer/iceland/" onclick="return clickMenu('sub_1_92');"> <span>Iceland</span></a>  <ul id="sub_1_92" class="hidden"><li id="t_26861" class="tournament">
                                            <a href="/soccer/iceland/pepsideild/">Pepsideild</a><span class="number"> (6)</span>  </li>
                                    <li id="t_26863" class="tournament">
                                            <a href="/soccer/iceland/division-2/">Division 2</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-228"> </span><a href="/soccer/indonesia/" onclick="return clickMenu('sub_1_228');"> <span>Indonesia</span></a>  <ul id="sub_1_228" class="hidden"><li id="t_32012" class="tournament">
                                            <a href="/soccer/indonesia/liga-1/">Liga 1</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32394" class="tournament">
                                            <a href="/soccer/indonesia/liga-2/">Liga 2</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-96"> </span><a href="/soccer/ireland/" onclick="return clickMenu('sub_1_96');"> <span>Ireland</span></a>  <ul id="sub_1_96" class="hidden"><li id="t_26750" class="tournament">
                                            <a href="/soccer/ireland/premier-division/">Premier Division</a><span class="number"> (4)</span>  </li>
                                    <li id="t_26501" class="tournament">
                                            <a href="/soccer/ireland/division-1/">Division 1</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-97"> </span><a href="/soccer/israel/" onclick="return clickMenu('sub_1_97');"> <span>Israel</span></a>  <ul id="sub_1_97" class="hidden"><li id="t_31981" class="tournament">
                                            <a href="/soccer/israel/ligat-ha-al/">Ligat ha'Al</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-98"> </span><a href="/soccer/italy/" onclick="return clickMenu('sub_1_98');"> <span>Italy</span></a>  <ul id="sub_1_98" class="hidden"><li id="t_32700" class="tournament">
                                            <a href="/soccer/italy/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-100"> </span><a href="/soccer/japan/" onclick="return clickMenu('sub_1_100');"> <span>Japan</span></a>  <ul id="sub_1_100" class="hidden"><li id="t_31226" class="tournament">
                                            <a href="/soccer/japan/j-league-division-2/">J-League Division 2</a><span class="number"> (11)</span>  </li>
                                    <li id="t_32329" class="tournament">
                                            <a href="/soccer/japan/emperors-cup/">Emperors Cup</a><span class="number"> (16)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-102"> </span><a href="/soccer/kazakhstan/" onclick="return clickMenu('sub_1_102');"> <span>Kazakhstan</span></a>  <ul id="sub_1_102" class="hidden"><li id="t_31453" class="tournament">
                                            <a href="/soccer/kazakhstan/premier-league/">Premier League</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-110"> </span><a href="/soccer/latvia/" onclick="return clickMenu('sub_1_110');"> <span>Latvia</span></a>  <ul id="sub_1_110" class="hidden"><li id="t_31323" class="tournament">
                                            <a href="/soccer/latvia/synottip-virsliga/">SynotTip Virslīga</a><span class="number"> (2)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-128"> </span><a href="/soccer/mexico/" onclick="return clickMenu('sub_1_128');"> <span>Mexico</span></a>  <ul id="sub_1_128" class="hidden"><li id="t_28471" class="tournament">
                                            <a href="/soccer/mexico/copa-mexico/">Copa Mexico</a><span class="number"> (1)</span>  </li>
                                    <li id="t_32628" class="tournament">
                                            <a href="/soccer/mexico/campeon-de-campeones/">Campeón de Campeones</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-139"> </span><a href="/soccer/netherlands/" onclick="return clickMenu('sub_1_139');"> <span>Netherlands</span></a>  <ul id="sub_1_139" class="hidden"><li id="t_28212" class="tournament">
                                            <a href="/soccer/netherlands/eredivisie/">Eredivisie</a><span class="number"> (9)</span>  </li>
                                    <li id="t_32450" class="tournament">
                                            <a href="/soccer/netherlands/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-2"> </span><a href="/soccer/north-central-america/" onclick="return clickMenu('sub_1_2');"> <span>North &amp; Central America</span></a>  <ul id="sub_1_2" class="hidden"><li id="t_30916" class="tournament">
                                            <a href="/soccer/north-central-america/gold-cup/">Gold Cup</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-145"> </span><a href="/soccer/norway/" onclick="return clickMenu('sub_1_145');"> <span>Norway</span></a>  <ul id="sub_1_145" class="hidden"><li id="t_26393" class="tournament">
                                            <a href="/soccer/norway/eliteserien/">Eliteserien</a><span class="number"> (17)</span>  </li>
                                    <li id="t_26392" class="tournament">
                                            <a href="/soccer/norway/obos-ligaen/">OBOS-ligaen</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32088" class="tournament">
                                            <a href="/soccer/norway/nm-cup/">NM Cup</a><span class="number"> (8)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-152"> </span><a href="/soccer/peru/" onclick="return clickMenu('sub_1_152');"> <span>Peru</span></a>  <ul id="sub_1_152" class="hidden"><li id="t_27530" class="tournament">
                                            <a href="/soccer/peru/primera-division/">Primera Division</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30782" class="tournament">
                                            <a href="/soccer/peru/segunda-division/">Segunda Division</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-153"> </span><a href="/soccer/philippines/" onclick="return clickMenu('sub_1_153');"> <span>Philippines</span></a>  <ul id="sub_1_153" class="hidden"><li id="t_32324" class="tournament">
                                            <a href="/soccer/philippines/pfl/">PFL</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-154"> </span><a href="/soccer/poland/" onclick="return clickMenu('sub_1_154');"> <span>Poland</span></a>  <ul id="sub_1_154" class="hidden"><li id="t_28365" class="tournament">
                                            <a href="/soccer/poland/ekstraklasa/">Ekstraklasa</a><span class="number"> (8)</span>  </li>
                                    
                                    
                                          </ul></li><li class="country"><span class="f f-155"> </span><a href="/soccer/portugal/" onclick="return clickMenu('sub_1_155');"> <span>Portugal</span></a>  <ul id="sub_1_155" class="hidden"><li id="t_28689" class="tournament">
                                            <a href="/soccer/portugal/primeira-liga/">Primeira Liga</a><span class="number"> (9)</span>  </li>
                                    <li id="t_32711" class="tournament">
                                            <a href="/soccer/portugal/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-157"> </span><a href="/soccer/romania/" onclick="return clickMenu('sub_1_157');"> <span>Romania</span></a>  <ul id="sub_1_157" class="hidden"><li id="t_28958" class="tournament">
                                            <a href="/soccer/romania/liga-1/">Liga 1</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-158"> </span><a href="/soccer/russia/" onclick="return clickMenu('sub_1_158');"> <span>Russia</span></a>  <ul id="sub_1_158" class="hidden"><li id="t_28225" class="tournament">
                                            <a href="/soccer/russia/premier-league/">Premier League</a><span class="number"> (16)</span>  </li>
                                    <li id="t_28321" class="tournament">
                                            <a href="/soccer/russia/division-1/">Division 1</a><span class="number"> (10)</span>  </li>
                                    <li id="t_32850" class="tournament">
                                            <a href="/soccer/russia/youth-league/">Youth League</a><span class="number"> (3)</span>  </li>
                                    <li id="t_32543" class="tournament">
                                            <a href="/soccer/russia/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-199"> </span><a href="/soccer/scotland/" onclick="return clickMenu('sub_1_199');"> <span>Scotland</span></a>  <ul id="sub_1_199" class="hidden"><li id="t_28259" class="tournament">
                                            <a href="/soccer/scotland/premiership/">Premiership</a><span class="number"> (6)</span>  </li>
                                    <li id="t_32762" class="tournament">
                                            <a href="/soccer/scotland/betfred-cup/">Betfred Cup</a><span class="number"> (16)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-170"> </span><a href="/soccer/singapore/" onclick="return clickMenu('sub_1_170');"> <span>Singapore</span></a>  <ul id="sub_1_170" class="hidden"><li id="t_33241" class="tournament">
                                            <a href="/soccer/singapore/league-cup/">League Cup</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-172"> </span><a href="/soccer/slovenia/" onclick="return clickMenu('sub_1_172');"> <span>Slovenia</span></a>  <ul id="sub_1_172" class="hidden"><li id="t_28398" class="tournament">
                                            <a href="/soccer/slovenia/prva-liga/">Prva liga</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-3"> </span><a href="/soccer/south-america/" onclick="return clickMenu('sub_1_3');"> <span>South America</span></a>  <ul id="sub_1_3" class="hidden"><li id="t_24825" class="tournament">
                                            <a href="/soccer/south-america/copa-libertadores/">Copa Libertadores</a><span class="number"> (8)</span>  </li>
                                    <li id="t_26901" class="tournament">
                                            <a href="/soccer/south-america/copa-sudamericana/">Copa Sudamericana</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-106"> </span><a href="/soccer/south-korea/" onclick="return clickMenu('sub_1_106');"> <span>South Korea</span></a>  <ul id="sub_1_106" class="hidden"><li id="t_26864" class="tournament">
                                            <a href="/soccer/south-korea/k-league-classic/">K-League Classic</a><span class="number"> (12)</span>  </li>
                                    <li id="t_26682" class="tournament">
                                            <a href="/soccer/south-korea/k-league-challenge/">K League Challenge</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-176"> </span><a href="/soccer/spain/" onclick="return clickMenu('sub_1_176');"> <span>Spain</span></a>  <ul id="sub_1_176" class="hidden"><li id="t_32621" class="tournament">
                                            <a href="/soccer/spain/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-181"> </span><a href="/soccer/sweden/" onclick="return clickMenu('sub_1_181');"> <span>Sweden</span></a>  <ul id="sub_1_181" class="hidden"><li id="t_26397" class="tournament">
                                            <a href="/soccer/sweden/allsvenskan/">Allsvenskan</a><span class="number"> (15)</span>  </li>
                                    <li id="t_26396" class="tournament">
                                            <a href="/soccer/sweden/superettan/">Superettan</a><span class="number"> (16)</span>  </li>
                                    <li id="t_30973" class="tournament">
                                            <a href="/soccer/sweden/division-1-norra/">Division 1 - Norra</a><span class="number"> (7)</span>  </li>
                                    <li id="t_30974" class="tournament">
                                            <a href="/soccer/sweden/division-1-sodra/">Division 1 - Södra</a><span class="number"> (7)</span>  </li>
                                    
                                    
                                    
                                    
                                    
                                    
                                    <li id="t_30930" class="tournament">
                                            <a href="/soccer/sweden/elitettan-women-2017/">Elitettan Women 2017</a><span class="number"> (2)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-182"> </span><a href="/soccer/switzerland/" onclick="return clickMenu('sub_1_182');"> <span>Switzerland</span></a>  <ul id="sub_1_182" class="hidden"><li id="t_28263" class="tournament">
                                            <a href="/soccer/switzerland/super-league/">Super League</a><span class="number"> (10)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-195"> </span><a href="/soccer/ukraine/" onclick="return clickMenu('sub_1_195');"> <span>Ukraine</span></a>  <ul id="sub_1_195" class="hidden"><li id="t_28701" class="tournament">
                                            <a href="/soccer/ukraine/pari-match-league/">Pari-Match League</a><span class="number"> (6)</span>  </li>
                                    <li id="t_32603" class="tournament">
                                            <a href="/soccer/ukraine/super-cup/">Super Cup</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-200"> </span><a href="/soccer/usa/" onclick="return clickMenu('sub_1_200');"> <span>USA</span></a>  <ul id="sub_1_200" class="hidden">
                                    <li id="t_31464" class="tournament">
                                            <a href="/soccer/usa/nasl/">NASL</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31350" class="tournament">
                                            <a href="/soccer/usa/usl-2017/">USL 2017</a><span class="number"> (2)</span>  </li>
                                    <li id="t_32142" class="tournament">
                                            <a href="/soccer/usa/us-open-cup/">US Open Cup</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-8"> </span><a href="/soccer/world/" onclick="return clickMenu('sub_1_8');"> <span>World</span></a>  <ul id="sub_1_8" class="hidden"><li id="t_22894" class="tournament">
                                            <a href="/soccer/world/world-cup-2018/">World Cup 2018</a><span class="number"> (34)</span>  </li>
                                    <li id="t_29783" class="tournament">
                                            <a href="/soccer/world/friendly-international/">Friendly International</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30424" class="tournament">
                                            <a href="/soccer/world/club-friendly/">Club Friendly</a><span class="number"> (96)</span>  </li>
                                    <li id="t_31828" class="tournament">
                                            <a href="/soccer/world/international-champions-cup/">International Champions Cup</a><span class="number"> (19)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/tennis/" onclick="return clickMenu('s_2');" class="siconleft s2">Tennis</a></div>
                                        <div id="s_2" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/tennis/">Today's matches</a></li><li class="country"><span class="f f-47"> </span><a href="/tennis/canada/" onclick="return clickMenu('sub_2_47');"> <span>Canada</span></a>  <ul id="sub_2_47"><li id="t_33272" class="tournament">
                                            <a href="/tennis/canada/winnipeg-challenger-men/">Winnipeg Challenger Men</a><span class="number"> (11)</span>  </li>
                                    <li id="t_33273" class="tournament">
                                            <a href="/tennis/canada/winnipeg-challenger-men-doubles/">Winnipeg Challenger Men Doubles</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-53"> </span><a href="/tennis/colombia/" onclick="return clickMenu('sub_2_53');"> <span>Colombia</span></a>  <ul id="sub_2_53"><li id="t_33274" class="tournament">
                                            <a href="/tennis/colombia/medellin-challenger-men/">Medellin Challenger Men</a><span class="number"> (12)</span>  </li>
                                    <li id="t_33275" class="tournament">
                                            <a href="/tennis/colombia/medellin-challenger-men-doubles/">Medellin Challenger Men Doubles</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-77"> </span><a href="/tennis/france/" onclick="return clickMenu('sub_2_77');"> <span>France</span></a>  <ul id="sub_2_77"><li id="t_33281" class="tournament">
                                            <a href="/tennis/france/itf-contrexeville-women/">ITF Contrexeville Women</a><span class="number"> (12)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-81"> </span><a href="/tennis/germany/" onclick="return clickMenu('sub_2_81');"> <span>Germany</span></a>  <ul id="sub_2_81"><li id="t_33266" class="tournament">
                                            <a href="/tennis/germany/braunschweig-challenger-men/">Braunschweig Challenger Men</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33267" class="tournament">
                                            <a href="/tennis/germany/braunschweig-challenger-men-doubles/">Braunschweig Challenger Men Doubles</a><span class="number"> (4)</span>  </li>
                                    <li id="t_33280" class="tournament">
                                            <a href="/tennis/germany/itf-trier-men/">ITF Trier Men</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33283" class="tournament">
                                            <a href="/tennis/germany/itf-versmold-women/">ITF Versmold Women</a><span class="number"> (11)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-91"> </span><a href="/tennis/hungary/" onclick="return clickMenu('sub_2_91');"> <span>Hungary</span></a>  <ul id="sub_2_91"><li id="t_33282" class="tournament">
                                            <a href="/tennis/hungary/itf-budapest-women/">ITF Budapest Women</a><span class="number"> (8)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-98"> </span><a href="/tennis/italy/" onclick="return clickMenu('sub_2_98');"> <span>Italy</span></a>  <ul id="sub_2_98"><li id="t_33278" class="tournament">
                                            <a href="/tennis/italy/itf-casinalbo-men/">ITF Casinalbo Men</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33276" class="tournament">
                                            <a href="/tennis/italy/perugia-challenger-men/">Perugia Challenger Men</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33277" class="tournament">
                                            <a href="/tennis/italy/perugia-challenger-men-doubles/">Perugia Challenger Men Doubles</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-176"> </span><a href="/tennis/spain/" onclick="return clickMenu('sub_2_176');"> <span>Spain</span></a>  <ul id="sub_2_176"><li id="t_33279" class="tournament">
                                            <a href="/tennis/spain/itf-gandia-men/">ITF Gandia Men</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-181"> </span><a href="/tennis/sweden/" onclick="return clickMenu('sub_2_181');"> <span>Sweden</span></a>  <ul id="sub_2_181"><li id="t_33270" class="tournament">
                                            <a href="/tennis/sweden/bastad-challenger-men/">Bastad Challenger Men</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33271" class="tournament">
                                            <a href="/tennis/sweden/bastad-challenger-men-doubles/">Bastad Challenger Men Doubles</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-197"> </span><a href="/tennis/united-kingdom/" onclick="return clickMenu('sub_2_197');"> <span>United Kingdom</span></a>  <ul id="sub_2_197"><li id="t_32984" class="tournament">
                                            <a href="/tennis/united-kingdom/atp-wimbledon/">ATP Wimbledon</a><span class="number"> (4)</span>  </li>
                                    <li id="t_32985" class="tournament">
                                            <a href="/tennis/united-kingdom/atp-wimbledon-doubles/">ATP Wimbledon Doubles</a><span class="number"> (5)</span>  </li>
                                    <li id="t_32986" class="tournament">
                                            <a href="/tennis/united-kingdom/wta-wimbledon/">WTA Wimbledon</a><span class="number"> (2)</span>  </li>
                                    <li id="t_32987" class="tournament">
                                            <a href="/tennis/united-kingdom/wta-wimbledon-doubles/">WTA Wimbledon Doubles</a><span class="number"> (4)</span>  </li>
                                    <li id="t_32988" class="tournament">
                                            <a href="/tennis/united-kingdom/wimbledon-mixed-doubles/">Wimbledon Mixed Doubles</a><span class="number"> (7)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-200"> </span><a href="/tennis/usa/" onclick="return clickMenu('sub_2_200');"> <span>USA</span></a>  <ul id="sub_2_200"><li id="t_33268" class="tournament">
                                            <a href="/tennis/usa/winnetka-challenger-men/">Winnetka Challenger Men</a><span class="number"> (9)</span>  </li>
                                    <li id="t_33269" class="tournament">
                                            <a href="/tennis/usa/winnetka-challenger-men-doubles/">Winnetka Challenger Men Doubles</a><span class="number"> (5)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/basketball/" onclick="return clickMenu('s_3');" class="siconleft s3">Basketball</a></div>
                                        <div id="s_3" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/basketball/">Today's matches</a></li><li class="country"><span class="f f-22"> </span><a href="/basketball/argentina/" onclick="return clickMenu('sub_3_22');"> <span>Argentina</span></a>  <ul id="sub_3_22" class="hidden"><li id="t_29522" class="tournament">
                                            <a href="/basketball/argentina/liga-a/">Liga A</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-6"> </span><a href="/basketball/europe/" onclick="return clickMenu('sub_3_6');"> <span>Europe</span></a>  <ul id="sub_3_6" class="hidden"><li id="t_32454" class="tournament">
                                            <a href="/basketball/europe/european-championship-u20-women/">European Championship U20 Women</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32455" class="tournament">
                                            <a href="/basketball/europe/european-championship-u20-b-women/">European Championship U20 B Women</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-2"> </span><a href="/basketball/north-central-america/" onclick="return clickMenu('sub_3_2');"> <span>North &amp; Central America</span></a>  <ul id="sub_3_2" class="hidden"><li id="t_33370" class="tournament">
                                            <a href="/basketball/north-central-america/centrobasket-championship-women/">Centrobasket Championship Women</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-236"> </span><a href="/basketball/puerto-rico/" onclick="return clickMenu('sub_3_236');"> <span>Puerto Rico</span></a>  <ul id="sub_3_236" class="hidden"><li id="t_31913" class="tournament">
                                            <a href="/basketball/puerto-rico/bsn/">BSN</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-200"> </span><a href="/basketball/usa/" onclick="return clickMenu('sub_3_200');"> <span>USA</span></a>  <ul id="sub_3_200" class="hidden"><li id="t_33099" class="tournament">
                                            <a href="/basketball/usa/nba-las-vegas-summer-league/">NBA Las Vegas Summer League</a><span class="number"> (9)</span>  </li>
                                    <li id="t_32247" class="tournament">
                                            <a href="/basketball/usa/wnba/">WNBA</a><span class="number"> (4)</span>  </li>
                                    <li id="t_33055" class="tournament">
                                            <a href="/basketball/usa/big3-3x3/">BIG3 (3x3)</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-8"> </span><a href="/basketball/world/" onclick="return clickMenu('sub_3_8');"> <span>World</span></a>  <ul id="sub_3_8" class="hidden"><li id="t_32489" class="tournament">
                                            <a href="/basketball/world/friendly-international/">Friendly International</a><span class="number"> (3)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/hockey/" onclick="return clickMenu('s_4');" class="siconleft s4">Hockey</a></div>
                                        <div id="s_4" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-24"> </span><a href="/hockey/australia/" onclick="return clickMenu('sub_4_24');"> <span>Australia</span></a>  <ul id="sub_4_24" class="hidden"><li id="t_31270" class="tournament">
                                            <a href="/hockey/australia/aihl/">AIHL</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-25"> </span><a href="/hockey/austria/" onclick="return clickMenu('sub_4_25');"> <span>Austria</span></a>  <ul id="sub_4_25" class="hidden"><li id="t_32701" class="tournament">
                                            <a href="/hockey/austria/ebel/">EBEL</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-140"> </span><a href="/hockey/new-zealand/" onclick="return clickMenu('sub_4_140');"> <span>New Zealand</span></a>  <ul id="sub_4_140" class="hidden"><li id="t_32843" class="tournament">
                                            <a href="/hockey/new-zealand/nzihl/">NZIHL</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-145"> </span><a href="/hockey/norway/" onclick="return clickMenu('sub_4_145');"> <span>Norway</span></a>  <ul id="sub_4_145" class="hidden"><li id="t_32899" class="tournament">
                                            <a href="/hockey/norway/get-ligaen/">Get-ligaen</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-158"> </span><a href="/hockey/russia/" onclick="return clickMenu('sub_4_158');"> <span>Russia</span></a>  <ul id="sub_4_158" class="hidden"><li id="t_33105" class="tournament">
                                            <a href="/hockey/russia/khl/">KHL</a><span class="number"> (13)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/handball/" onclick="return clickMenu('s_7');" class="siconleft s7">Handball</a></div>
                                        <div id="s_7" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/handball/">Today's matches</a></li><li class="country"><span class="f f-106"> </span><a href="/handball/south-korea/" onclick="return clickMenu('sub_7_106');"> <span>South Korea</span></a>  <ul id="sub_7_106" class="hidden"><li id="t_31266" class="tournament">
                                            <a href="/handball/south-korea/1st-league/">1st League</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31264" class="tournament">
                                            <a href="/handball/south-korea/1st-league-women/">1st League Women</a><span class="number"> (1)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/baseball/" onclick="return clickMenu('s_6');" class="siconleft s6">Baseball</a></div>
                                        <div id="s_6" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/baseball/">Today's matches</a></li><li class="country"><span class="f f-100"> </span><a href="/baseball/japan/" onclick="return clickMenu('sub_6_100');"> <span>Japan</span></a>  <ul id="sub_6_100" class="hidden"><li id="t_30868" class="tournament">
                                            <a href="/baseball/japan/npb/">NPB</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-128"> </span><a href="/baseball/mexico/" onclick="return clickMenu('sub_6_128');"> <span>Mexico</span></a>  <ul id="sub_6_128" class="hidden"><li id="t_31948" class="tournament">
                                            <a href="/baseball/mexico/lmb/">LMB</a><span class="number"> (14)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-139"> </span><a href="/baseball/netherlands/" onclick="return clickMenu('sub_6_139');"> <span>Netherlands</span></a>  <ul id="sub_6_139" class="hidden"><li id="t_31991" class="tournament">
                                            <a href="/baseball/netherlands/hoofdklasse/">Hoofdklasse</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-106"> </span><a href="/baseball/south-korea/" onclick="return clickMenu('sub_6_106');"> <span>South Korea</span></a>  <ul id="sub_6_106" class="hidden"><li id="t_30917" class="tournament">
                                            <a href="/baseball/south-korea/kbo/">KBO</a><span class="number"> (5)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-218"> </span><a href="/baseball/taiwan/" onclick="return clickMenu('sub_6_218');"> <span>Taiwan</span></a>  <ul id="sub_6_218" class="hidden"><li id="t_31791" class="tournament">
                                            <a href="/baseball/taiwan/cpbl/">CPBL</a><span class="number"> (1)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-200"> </span><a href="/baseball/usa/" onclick="return clickMenu('sub_6_200');"> <span>USA</span></a>  <ul id="sub_6_200" class="hidden">
                                    <li id="t_31283" class="tournament">
                                            <a href="/baseball/usa/il/">IL</a><span class="number"> (7)</span>  </li>
                                    <li id="t_31144" class="tournament">
                                            <a href="/baseball/usa/pcl/">PCL</a><span class="number"> (8)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/american-football/" onclick="return clickMenu('s_5');" class="siconleft s5">American Football</a></div>
                                        <div id="s_5" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-25"> </span><a href="/american-football/austria/" onclick="return clickMenu('sub_5_25');"> <span>Austria</span></a>  <ul id="sub_5_25" class="hidden"><li id="t_31713" class="tournament">
                                            <a href="/american-football/austria/afl/">AFL</a><span class="number"> (2)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-47"> </span><a href="/american-football/canada/" onclick="return clickMenu('sub_5_47');"> <span>Canada</span></a>  <ul id="sub_5_47" class="hidden"><li id="t_32462" class="tournament">
                                            <a href="/american-football/canada/cfl/">CFL</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-200"> </span><a href="/american-football/usa/" onclick="return clickMenu('sub_5_200');"> <span>USA</span></a>  <ul id="sub_5_200" class="hidden"><li id="t_32224" class="tournament">
                                            <a href="/american-football/usa/nfl/">NFL</a><span class="number"> (17)</span>  </li>
                                    <li id="t_32311" class="tournament">
                                            <a href="/american-football/usa/ncaa/">NCAA</a><span class="number"> (77)</span>  </li>
                                    <li id="t_31763" class="tournament">
                                            <a href="/american-football/usa/afl/">AFL</a><span class="number"> (2)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/rugby-union/" onclick="return clickMenu('s_8');" class="siconleft s8">Rugby Union</a></div>
                                        <div id="s_8" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-8"> </span><a href="/rugby-union/world/" onclick="return clickMenu('sub_8_8');"> <span>World</span></a>  <ul id="sub_8_8" class="hidden"><li id="t_30282" class="tournament">
                                            <a href="/rugby-union/world/super-rugby/">Super Rugby</a><span class="number"> (9)</span>  </li>
                                    
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/rugby-league/" onclick="return clickMenu('s_19');" class="siconleft s19">Rugby League</a></div>
                                        <div id="s_19" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/rugby-league/">Today's matches</a></li><li class="country"><span class="f f-24"> </span><a href="/rugby-league/australia/" onclick="return clickMenu('sub_19_24');"> <span>Australia</span></a>  <ul id="sub_19_24" class="hidden"><li id="t_31304" class="tournament">
                                            <a href="/rugby-league/australia/nrl/">NRL</a><span class="number"> (14)</span>  </li>
                                    <li id="t_31340" class="tournament">
                                            <a href="/rugby-league/australia/state-of-origin/">State of Origin</a><span class="number"> (1)</span>  </li>
                                    
                                    
                                          </ul></li><li class="country"><span class="f f-198"> </span><a href="/rugby-league/england/" onclick="return clickMenu('sub_19_198');"> <span>England</span></a>  <ul id="sub_19_198" class="hidden"><li id="t_28913" class="tournament">
                                            <a href="/rugby-league/england/super-league/">Super League</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-6"> </span><a href="/rugby-league/europe/" onclick="return clickMenu('sub_19_6');"> <span>Europe</span></a>  <ul id="sub_19_6" class="hidden"><li id="t_31333" class="tournament">
                                            <a href="/rugby-league/europe/challenge-cup/">Challenge Cup</a><span class="number"> (2)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/volleyball/" onclick="return clickMenu('s_12');" class="siconleft s12">Volleyball</a></div>
                                        <div id="s_12" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/volleyball/">Today's matches</a></li><li class="country"><span class="f f-8"> </span><a href="/volleyball/world/" onclick="return clickMenu('sub_12_8');"> <span>World</span></a>  <ul id="sub_12_8" class="hidden"><li id="t_32526" class="tournament">
                                            <a href="/volleyball/world/world-championship/">World Championship</a><span class="number"> (4)</span>  </li>
                                    <li id="t_28001" class="tournament">
                                            <a href="/volleyball/world/world-grand-prix-women/">World Grand Prix Women</a><span class="number"> (6)</span>  </li>
                                    <li id="t_32374" class="tournament">
                                            <a href="/volleyball/world/friendly-international/">Friendly International</a><span class="number"> (2)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/cricket/" onclick="return clickMenu('s_13');" class="siconleft s13">Cricket</a></div>
                                        <div id="s_13" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/cricket/">Today's matches</a></li><li class="country"><span class="f f-197"> </span><a href="/cricket/united-kingdom/" onclick="return clickMenu('sub_13_197');"> <span>United Kingdom</span></a>  <ul id="sub_13_197" class="hidden"><li id="t_32773" class="tournament">
                                            <a href="/cricket/united-kingdom/natwest-t20-blast/">NatWest T20 Blast</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-8"> </span><a href="/cricket/world/" onclick="return clickMenu('sub_13_8');"> <span>World</span></a>  <ul id="sub_13_8" class="hidden"><li id="t_26135" class="tournament">
                                            <a href="/cricket/world/test-series/">Test Series</a><span class="number"> (2)</span>  </li>
                                    <li id="t_31141" class="tournament">
                                            <a href="/cricket/world/the-ashes/">The Ashes</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31275" class="tournament">
                                            <a href="/cricket/world/icc-world-cup-women/">ICC World Cup Women</a><span class="number"> (3)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/snooker/" onclick="return clickMenu('s_15');" class="siconleft s15">Snooker</a></div>
                                        <div id="s_15" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-222"> </span><a href="/snooker/hong-kong/" onclick="return clickMenu('sub_15_222');"> <span>Hong Kong</span></a>  <ul id="sub_15_222" class="hidden"><li id="t_32965" class="tournament">
                                            <a href="/snooker/hong-kong/hong-kong-masters/">Hong Kong Masters</a><span class="number"> (4)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/darts/" onclick="return clickMenu('s_14');" class="siconleft s14">Darts</a></div>
                                        <div id="s_14" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-8"> </span><a href="/darts/world/" onclick="return clickMenu('sub_14_8');"> <span>World</span></a>  <ul id="sub_14_8" class="hidden"><li id="t_33366" class="tournament">
                                            <a href="/darts/world/world-matchplay/">World Matchplay</a><span class="number"> (16)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/boxing/" onclick="return clickMenu('s_16');" class="siconleft s16">Boxing</a></div>
                                        <div id="s_16" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-8"> </span><a href="/boxing/world/" onclick="return clickMenu('sub_16_8');"> <span>World</span></a>  <ul id="sub_16_8" class="hidden"><li id="t_31254" class="tournament">
                                            <a href="/boxing/world/super-lightweight-others-matches-men/">Super Lightweight - Others matches Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31103" class="tournament">
                                            <a href="/boxing/world/featherweight-ibf-title-men/">Featherweight - IBF Title Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_32225" class="tournament">
                                            <a href="/boxing/world/super-middleweight-others-matches-men/">Super Middleweight - Others matches Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_31249" class="tournament">
                                            <a href="/boxing/world/welterweight-others-matches-men/">Welterweight - Others matches Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_32414" class="tournament">
                                            <a href="/boxing/world/middleweight-wbc-ibf-wbo-wba-super-titles-men/">Middleweight - WBC/IBF/WBO/WBA Super Titles Men</a><span class="number"> (1)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/beach-volleyball/" onclick="return clickMenu('s_17');" class="siconleft s17">Beach Volleyball</a></div>
                                        <div id="s_17" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/beach-volleyball/">Today's matches</a></li><li class="country"><span class="f f-8"> </span><a href="/beach-volleyball/world/" onclick="return clickMenu('sub_17_8');"> <span>World</span></a>  <ul id="sub_17_8"><li id="t_33336" class="tournament">
                                            <a href="/beach-volleyball/world/world-championship-u21-men/">World Championship U21 Men</a><span class="number"> (5)</span>  </li>
                                    <li id="t_33337" class="tournament">
                                            <a href="/beach-volleyball/world/world-championship-u21-women/">World Championship U21 Women</a><span class="number"> (12)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/aussie-rules/" onclick="return clickMenu('s_18');" class="siconleft s18">Aussie Rules</a></div>
                                        <div id="s_18" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-24"> </span><a href="/aussie-rules/australia/" onclick="return clickMenu('sub_18_24');"> <span>Australia</span></a>  <ul id="sub_18_24" class="hidden"><li id="t_30295" class="tournament">
                                            <a href="/aussie-rules/australia/afl/">AFL</a><span class="number"> (18)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/badminton/" onclick="return clickMenu('s_21');" class="siconleft s21">Badminton</a></div>
                                        <div id="s_21" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/badminton/">Today's matches</a></li><li class="country"><span class="f f-47"> </span><a href="/badminton/canada/" onclick="return clickMenu('sub_21_47');"> <span>Canada</span></a>  <ul id="sub_21_47" class="hidden"><li id="t_33181" class="tournament">
                                            <a href="/badminton/canada/grand-prix-canada-open-doubles-men/">Grand Prix Canada Open Doubles Men</a><span class="number"> (13)</span>  </li>
                                    <li id="t_33182" class="tournament">
                                            <a href="/badminton/canada/grand-prix-canada-open-doubles-women/">Grand Prix Canada Open Doubles Women</a><span class="number"> (13)</span>  </li>
                                    <li id="t_33179" class="tournament">
                                            <a href="/badminton/canada/grand-prix-canada-open-men/">Grand Prix Canada Open Men</a><span class="number"> (38)</span>  </li>
                                    <li id="t_33183" class="tournament">
                                            <a href="/badminton/canada/grand-prix-canada-open-mixed-doubles/">Grand Prix Canada Open Mixed Doubles</a><span class="number"> (14)</span>  </li>
                                    <li id="t_33180" class="tournament">
                                            <a href="/badminton/canada/grand-prix-canada-open-women/">Grand Prix Canada Open Women</a><span class="number"> (15)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/water-polo/" onclick="return clickMenu('s_22');" class="siconleft s22">Water polo</a></div>
                                        <div id="s_22" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-8"> </span><a href="/water-polo/world/" onclick="return clickMenu('sub_22_8');"> <span>World</span></a>  <ul id="sub_22_8" class="hidden"><li id="t_32296" class="tournament">
                                            <a href="/water-polo/world/world-championship/">World Championship</a><span class="number"> (8)</span>  </li>
                                    <li id="t_32297" class="tournament">
                                            <a href="/water-polo/world/world-championship-women/">World Championship Women</a><span class="number"> (8)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/pesapallo/" onclick="return clickMenu('s_30');" class="siconleft s30">Pesäpallo</a></div>
                                        <div id="s_30" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/pesapallo/">Today's matches</a></li><li class="country"><span class="f f-76"> </span><a href="/pesapallo/finland/" onclick="return clickMenu('sub_30_76');"> <span>Finland</span></a>  <ul id="sub_30_76" class="hidden"><li id="t_31783" class="tournament">
                                            <a href="/pesapallo/finland/ykkospesis/">Ykköspesis</a><span class="number"> (4)</span>  </li>
                                    <li id="t_31782" class="tournament">
                                            <a href="/pesapallo/finland/superpesis-women/">Superpesis Women</a><span class="number"> (4)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/esports/" onclick="return clickMenu('s_36');" class="siconleft s36">eSports</a></div>
                                        <div id="s_36" class="hidden">
                                            <ul>
                                <li><span class="f f-todays-matches"> </span><a href="/matches/esports/">Today's matches</a></li><li class="country"><span class="f f-52"> </span><a href="/esports/china/" onclick="return clickMenu('sub_36_52');"> <span>China</span></a>  <ul id="sub_36_52" class="hidden"><li id="t_31098" class="tournament">
                                            <a href="/esports/china/league-of-legends-lol-pro-league/">League of Legends LoL Pro League</a><span class="number"> (9)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-154"> </span><a href="/esports/poland/" onclick="return clickMenu('sub_36_154');"> <span>Poland</span></a>  <ul id="sub_36_154" class="hidden"><li id="t_33184" class="tournament">
                                            <a href="/esports/poland/counter-strike-pgl-major-krakow/">Counter-Strike PGL Major Krakow</a><span class="number"> (8)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-106"> </span><a href="/esports/south-korea/" onclick="return clickMenu('sub_36_106');"> <span>South Korea</span></a>  <ul id="sub_36_106" class="hidden"><li id="t_31137" class="tournament">
                                            <a href="/esports/south-korea/league-of-legends-champions-korea/">League of Legends Champions Korea</a><span class="number"> (8)</span>  </li>
                                    <li id="t_33171" class="tournament">
                                            <a href="/esports/south-korea/starcraft-2-global-starcraft-ii-league-season-3/">Starcraft 2 Global StarCraft II League - Season 3</a><span class="number"> (3)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-176"> </span><a href="/esports/spain/" onclick="return clickMenu('sub_36_176');"> <span>Spain</span></a>  <ul id="sub_36_176" class="hidden"><li id="t_33112" class="tournament">
                                            <a href="/esports/spain/counter-strike-dreamhack-valencia/">Counter-Strike DreamHack - Valencia</a><span class="number"> (4)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-218"> </span><a href="/esports/taiwan/" onclick="return clickMenu('sub_36_218');"> <span>Taiwan</span></a>  <ul id="sub_36_218" class="hidden"><li id="t_31019" class="tournament">
                                            <a href="/esports/taiwan/league-of-legends-lol-master-series/">League of Legends Lol Master Series</a><span class="number"> (6)</span>  </li>
                                          </ul></li><li class="country"><span class="f f-8"> </span><a href="/esports/world/" onclick="return clickMenu('sub_36_8');"> <span>World</span></a>  <ul id="sub_36_8" class="hidden"><li id="t_31166" class="tournament">
                                            <a href="/esports/world/league-of-legends-championship-series/">League of Legends Championship Series</a><span class="number"> (16)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    
                                    <li class="sport"><div class="sport_name"><a href="/mma/" onclick="return clickMenu('s_28');" class="siconleft s28">MMA</a></div>
                                        <div id="s_28" class="hidden">
                                            <ul>
                                <li class="country"><span class="f f-8"> </span><a href="/mma/world/" onclick="return clickMenu('sub_28_8');"> <span>World</span></a>  <ul id="sub_28_8" class="hidden"><li id="t_30405" class="tournament">
                                            <a href="/mma/world/bantamweight-ufc-men/">Bantamweight - UFC Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30749" class="tournament">
                                            <a href="/mma/world/featherweight-ufc-men/">Featherweight - UFC Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30750" class="tournament">
                                            <a href="/mma/world/flyweight-ufc-men/">Flyweight - UFC Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30404" class="tournament">
                                            <a href="/mma/world/heavyweight-ufc-men/">Heavyweight - UFC Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30292" class="tournament">
                                            <a href="/mma/world/light-heavyweight-ufc-men/">Light Heavyweight - UFC Men</a><span class="number"> (4)</span>  </li>
                                    <li id="t_30827" class="tournament">
                                            <a href="/mma/world/lightweight-bellator-men/">Lightweight - Bellator Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30426" class="tournament">
                                            <a href="/mma/world/lightweight-ufc-men/">Lightweight - UFC Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30785" class="tournament">
                                            <a href="/mma/world/middleweight-bellator-men/">Middleweight - Bellator Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30734" class="tournament">
                                            <a href="/mma/world/middleweight-ufc-men/">Middleweight - UFC Men</a><span class="number"> (2)</span>  </li>
                                    <li id="t_30425" class="tournament">
                                            <a href="/mma/world/welterweight-ufc-men/">Welterweight - UFC Men</a><span class="number"> (5)</span>  </li>
                                    <li id="t_30882" class="tournament">
                                            <a href="/mma/world/bantamweight-bellator-men/">Bantamweight - Bellator Men</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30849" class="tournament">
                                            <a href="/mma/world/bantamweight-ufc-women/">Bantamweight - UFC Women</a><span class="number"> (1)</span>  </li>
                                    <li id="t_31021" class="tournament">
                                            <a href="/mma/world/flyweight-bellator-women/">Flyweight - Bellator Women</a><span class="number"> (1)</span>  </li>
                                    <li id="t_30840" class="tournament">
                                            <a href="/mma/world/strawweight-ufc-women/">Strawweight - UFC Women</a><span class="number"> (1)</span>  </li>
                                          </ul></li>
                                        </ul>
                                    </div>
                                </li>
                    </ul><div class="spacer10"></div></div>
                    <!-- END SPORT MENU -->
                    <div class="spacer10"></div>

                    <hr class="hidden" />
                </div>
                            </div>
                <!-- END LEFT MENU -->

                <!-- RIGHT MENU -->

                                <div id="col-right">
                    
    <div id="my-box">
        <div class="head">
            <div class="head-bottom" id="head-coupon-bottom">
                <h2 class="coupon"><a href="/coupon">My Coupon</a> <span id="coupon-outcomes-count"></span></h2>
                <a href="#" onclick="globals.coupon.getActive().truncate()" class="coupon-arrow" id="coupon-arrow"> </a>
            </div>
        </div>

        <div id="my-coupon-container"><ul><li class="coupon-empty-info"><p>No bets selected yet. To add a bet click the odds while browsing through OddsPortal!</p></li></ul><div class="coupon-footer"><span class="all-white"><a href="/login">Log in to save and share your coupons.</a></span></div></div>
    </div>

        <div id="country-tournaments-widget" class="corner-box3">
        <div class="spc dark">
            <div class="head">
                <div class="dark-title hiconright"><h2><span class="siconright sr3">USA                 (Basketball)</span></h2></div>
            </div>

            <div class="box body"><ul class="rightSportMenu"><li><span class="f f-200"> </span> 
                                            <a href="/basketball/usa/nba-las-vegas-summer-league/">NBA Las Vegas Summer League</a><span class="number"> (9)</span>  </li><li><span class="f f-200"> </span> 
                                            <a href="/basketball/usa/wnba/">WNBA</a><span class="number"> (4)</span>  </li><li><span class="f f-200"> </span> 
                                            <a href="/basketball/usa/big3-3x3/">BIG3 (3x3)</a><span class="number"> (4)</span>  </li></ul></div>

            <div class="corner-box">
                <div class="spc light">
                    <div class="body">
                        <p class="all">
                            <a href="/basketball/usa/">USA</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
        <div class="corner-box">
        <div class="spc dark2">
            <div class="head">
                <div class="dark-title"><h2>Betting Tools</h2></div>
            </div>

            <table>
                                <tbody><tr>
                    <td class="bold">
                        <div id="bt-dropping-odds"> </div>
                        <a href="/dropping-odds/">Dropping Odds</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-blocked-games"> </div>
                        <a href="/blocked/">Blocked Odds</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-value-bets"> </div>
                        <a href="/value-bets/">Value Bets</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-hot-matches"> </div>
                        <a href="/hot-matches/">Hot Matches</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-divergent-margins"> </div>
                        <a href="/handicaps/">Best Handicaps</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-moving-margins"> </div>
                        <a href="/moving-margins/">Moving Margins</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-odds-archive"> </div>
                        <a href="/results/">Archived Results</a></td>
                </tr>
                                <tr>
                    <td class="bold">
                        <div id="bt-all-events-standings"> </div>
                        <a href="/standings/">Standings</a></td>
                </tr>
                            </tbody></table>


            <div class="corner-box">
                <div class="spc light">
                    <div class="body">
                        <p class="all"></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
                <div class="corner-box-no-margin">
<div class="adsenvelope banx-right_menu" id="lsadvert-zid-1041" style="width:235px;"><div style="height:235px"><div class="adsclick" style="width: 100% !important; height: 100% !important" onclick="window.open('https://ads.livesportmedia.eu/www/delivery/ck.php?oaparams=2__bannerid=32714__zoneid=1041', 'banner')"></div><div class="adscontent" id="lsadvert-right_menu"><iframe id="lsadvert-zid-1041-iframe" name="banx-right_menu" frameborder="0" scrolling="no" style="width: 235px; height: 235px;"></iframe></div></div></div><div class="adstext"><span>advertisement</span></div>          </div>
    <div class="corner-box3">
        <div class="spc dark">
            <div class="head">
                <div class="dark-title"><h2>Top Events</h2></div>
            </div>
            <div id="top-event-box" class="box body">
                <table class="table-main top-event">
                                                                            <tbody><tr class="odd">
                                    
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s1" href="/soccer/europe/euro-u19/">Euro U19</a></span>
                        </div>
                    </td>

                                                                                
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s1" href="/soccer/europe/champions-league/">Champs League</a></span>
                        </div>
                    </td>

                                                                                </tr>
                                                                                                                                    <tr class="even">
                                    
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s1" href="/soccer/europe/europa-league/">Europa League</a></span>
                        </div>
                    </td>

                                                                                
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s1" href="/soccer/world/club-friendly/">Club Friendly</a></span>
                        </div>
                    </td>

                                                                                </tr>
                                                                                                                                    <tr class="odd">
                                    
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s2" href="/tennis/united-kingdom/atp-wimbledon/">ATP Wimbledon</a></span>
                        </div>
                    </td>

                                                                                
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s2" href="/tennis/united-kingdom/wta-wimbledon/">WTA Wimbledon</a></span>
                        </div>
                    </td>

                                                                                </tr>
                                                                                                                                    <tr class="even">
                                    
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s6" href="/baseball/usa/mlb/">MLB</a></span>
                        </div>
                    </td>

                                                                                
                    <td class="column overflow">
                        <div class="overflow">
                            <span class="event"><a class="sicona s18" href="/aussie-rules/australia/afl/">AFL</a></span>
                        </div>
                    </td>

                                                                                </tr>
                                                                            
                                    </tbody></table>
            </div>

            <div class="corner-box">
                <div class="spc light">
                    <div class="body">
                        <p class="all">
                            <a href="/events/">All events</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
            <div class="corner-box">
            <div class="spc dark2">
                <div class="head">
                    <div class="dark-title"><h2 class="ico-bonus">RebelBetting</h2></div>
                </div>

                <table>
                    <tbody><tr>
                        <td>
                            <table class="rm-bonus-offer">
                                <colgroup><col width="1%" />
                                <col width="99%" />
                                </colgroup><tbody><tr>
                                    <td valign="top" class="logo">
                                        <!--  <a onclick="window.open(this.href); return false;" href="http://RebelBetting.com/?x=oddsportal" class="bb bb-rebelbetting" title="Try RebelBetting for FREE" rel="nofollow"></a>-->
                                        <a href="/professional-sure-bets/" class="bb bb-rebelbetting" title="Try RebelBetting for FREE" rel="nofollow"></a>
                                    </td>

                                    <td class="desc">
                                        <!--  <a onclick="window.open(this.href); return false;" href="http://RebelBetting.com/?x=oddsportal" title="Try RebelBetting for FREE" rel="nofollow">-->
                                        <a href="/professional-sure-bets/" title="Try RebelBetting for FREE" rel="nofollow">
                                            <span class="bold">Try RebelBetting for FREE</span>
                                        </a>

                                        <div class="break"></div>
                                        Increase your investment by 10-20%. Learn everything you need to know about sure bets and <span class="bold">make profit now!</span>
                                    </td>
                                </tr>
                            </tbody></table>

                        </td>
                    </tr>
                </tbody></table>


                <div class="corner-box">
                    <div class="spc light">
                        <div class="body">
                            <p class="all">
                                <a href="/professional-sure-bets/">Read more</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="corner-box">
            <div class="spc dark2">
                <div class="head">
                    <div class="dark-title"><h2 class="ico-bonus">Skrill VIP</h2></div>
                </div>

                <table>
                    <tbody><tr>
                        <td>
                            <table class="rm-bonus-offer">
                                <colgroup><col width="1%" />
                                <col width="99%" />
                                </colgroup><tbody><tr>
                                    <td valign="top" class="logo">
                                        <a onclick="window.open(this.href); return false;" href="http://wlskrill.adsrv.eacdn.com/C.ashx?btag=a_42656b_3273c_&amp;affid=38004&amp;siteid=42656&amp;adid=3273&amp;c=3278" class="bb bb-skrill" title="Get €100 Bonus!" rel="nofollow"></a>
                                    </td>

                                    <td class="desc">
                                        <a onclick="window.open(this.href); return false;" href="http://wlskrill.adsrv.eacdn.com/C.ashx?btag=a_40381b_3315c_&amp;affid=38004&amp;siteid=40381&amp;adid=3315&amp;c=" title="Get €100 Bonus!" rel="nofollow">
                                            <span class="bold">Get €100 Bonus!</span>
                                        </a>

                                        <div class="break"></div>
                                            Transact €3,000 or more within a 30 days period and you not only get Skrill VIP status, you also get up to €100 cash bonus!
                                    </td>
                                </tr>
                            </tbody></table>

                        </td>
                    </tr>
                </tbody></table>


                <div class="corner-box">
                    <div class="spc light">
                        <div class="body">
                            <p class="all">
                                <a href="/skrill/">Read more</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            <div class="rm-banner no-logged">
                <a class="multi-line-button" href="/register/" title="Join OddsPortal.com today and get all the benefits of Odds Portal membership.">
                    <span class="line-top">REGISTER</span>
                    <span class="line-normal">your account and</span>
                    <span class="line-normal highlight-off">CUSTOMIZE OddsPortal</span>
                    <span class="line-normal">to your needs!</span>
                </a>
            </div>
                            </div>
                

                <div class="break"></div>
                <hr class="hidden" />
            </div>
            <!-- END RIGHT MENU -->

            <!-- FOOTER -->
            <div id="footer">

                                <p>
                        <span class="r footer">
                            <a href="/faq/">FAQ</a> |
                            <a href="/site-map-active/">Site map</a> |
                            <a href="/terms/">Terms of Use</a> |
                            <a href="/privacy-policy/">Privacy Policy</a> |
                            <a href="/widgets/next-matches/">Widgets</a> |
                            <a href="/webmasters/">Webmasters</a> |
                                                        <a href="/contact/">Contact</a>
                        </span>

                    <span class="l footer">Copyright © 2008-17 OddsPortal.com<span id="status-dot" class="status-dot-green"></span></span>

                        <span>

                            <a class="twitter" rel="nofollow" onclick="window.open(this.href); return false;" href="/redirect/?url=http://www.twitter.com/oddsportal"></a>
                            <a class="googleplus" rel="nofollow" onclick="window.open(this.href); return false;" href="/redirect/?url=http://plus.google.com/106001884959424486346"></a>
                            <a class="facebook" rel="nofollow" onclick="window.open(this.href); return false;" href="/redirect/?url=http://www.facebook.com/OddsPortal"></a>
                            <a class="gpwa" rel="nofollow" onclick="window.open(this.href); return false;" href="/redirect/?url=http://certify.gpwa.org/verify/oddsportal.com/"></a>
                        </span>
                </p>

                <div class="break"></div>
                            </div>
        </div>
    </div>

    <span class="cor-l-t"> </span>
    <span class="cor-r-t"> </span>
    <span class="cor-l-b"> </span>
    <span class="cor-r-b"> </span>

    <div class="break"></div>
    <a id="scroll-to-top" style="display:none;"><span>Top</span></a>
</div>
</div>
</div>
</div>


<script type="text/javascript">
    //&lt;![CDATA[
    var op = new OpHandler();if(!page)var page = new PageTournament({"id":"KvGDOydm","sid":3,"cid":200,"archive":true});var menu_open = null;vJs();op.init();if(page &amp;&amp; page.display)page.display();    var sigEndPage = true;
    try
    {
        if (sigEndJs)
        {
            globals.onPageReady();
        }
    } catch (e)
    {
    }

    //]]&gt;
</script><div class="autofill_body" style="top: 400.203px; left: 44px; width: 131px;"><div class="autofill_body_content"></div></div>
                <script type="text/javascript">
                // &lt;![CDATA[
                var banners; 
                banners = new BannerHandler([254,1041,523,1877], [], window.bannersAdsServers || ["content.livesportmedia.eu"], [], $, "", null, null);

                
                document.lsadvert_display = function() {
                    banners.display();
                }
                                // ]]&gt;
                </script>
                <script type="text/javascript">if(typeof banners != 'undefined'){banners.addSetBackgroundCallback(function(){$('#top-right-social-column').hide();$('#right-ad-column').hide();});document.lsadvert_display();}</script>
<!-- DEBUG -->
<!-- END DEBUG -->
<span id="mlc-4ck3s9wd8c"></span>
<span id="mlc-aks81bkdz"></span>


<script type="text/javascript" id="">(function(h,a,c){"undefined"!==typeof module&amp;&amp;module.exports?module.exports=c():"function"===typeof define&amp;&amp;define.amd?define(c):a[h]=c()})("Fingerprint",this,function(){var h=function(a){var c,f;c=Array.prototype.forEach;f=Array.prototype.map;this.each=function(a,b,f){if(null!==a)if(c&amp;&amp;a.forEach===c)a.forEach(b,f);else if(a.length===+a.length)for(var e=0,d=a.length;e&lt;d&amp;&amp;b.call(f,a[e],e,a)!=={};e++);else for(e in a)if(a.hasOwnProperty(e)&amp;&amp;b.call(f,a[e],e,a)==={})break};this.map=function(a,b,c){var e=
[];if(null==a)return e;if(f&amp;&amp;a.map===f)return a.map(b,c);this.each(a,function(a,f,k){e[e.length]=b.call(c,a,f,k)});return e};"object"==typeof a?(this.hasher=a.hasher,this.screen_resolution=a.screen_resolution,this.screen_orientation=a.screen_orientation,this.canvas=a.canvas,this.ie_activex=a.ie_activex):"function"==typeof a&amp;&amp;(this.hasher=a)};h.prototype={get:function(){var a=[];a.push(navigator.userAgent);a.push(navigator.language);a.push(screen.colorDepth);if(this.screen_resolution){var c=this.getScreenResolution();
"undefined"!==typeof c&amp;&amp;a.push(c.join("x"))}a.push((new Date).getTimezoneOffset());a.push(this.hasSessionStorage());a.push(this.hasLocalStorage());a.push(this.hasIndexDb());document.body?a.push(typeof document.body.addBehavior):a.push("undefined");a.push(typeof window.openDatabase);a.push(navigator.cpuClass);a.push(navigator.platform);a.push(navigator.doNotTrack);a.push(this.getPluginsString());this.canvas&amp;&amp;this.isCanvasSupported()&amp;&amp;a.push(this.getCanvasFingerprint());return this.hasher?this.hasher(a.join("###"),
31):this.murmurhash3_32_gc(a.join("###"),31)},murmurhash3_32_gc:function(a,c){var f,h,b,k,e,d,g;f=a.length&amp;3;h=a.length-f;b=c;k=3432918353;e=461845907;for(g=0;g&lt;h;)d=a.charCodeAt(g)&amp;255|(a.charCodeAt(++g)&amp;255)&lt;&lt;8|(a.charCodeAt(++g)&amp;255)&lt;&lt;16|(a.charCodeAt(++g)&amp;255)&lt;&lt;24,++g,d=(d&amp;65535)*k+(((d&gt;&gt;&gt;16)*k&amp;65535)&lt;&lt;16)&amp;4294967295,d=d&lt;&lt;15|d&gt;&gt;&gt;17,d=(d&amp;65535)*e+(((d&gt;&gt;&gt;16)*e&amp;65535)&lt;&lt;16)&amp;4294967295,b^=d,b=b&lt;&lt;13|b&gt;&gt;&gt;19,b=5*(b&amp;65535)+((5*(b&gt;&gt;&gt;16)&amp;65535)&lt;&lt;16)&amp;4294967295,b=(b&amp;65535)+27492+(((b&gt;&gt;&gt;16)+58964&amp;65535)&lt;&lt;
16);d=0;switch(f){case 3:d^=(a.charCodeAt(g+2)&amp;255)&lt;&lt;16;case 2:d^=(a.charCodeAt(g+1)&amp;255)&lt;&lt;8;case 1:d^=a.charCodeAt(g)&amp;255,d=(d&amp;65535)*k+(((d&gt;&gt;&gt;16)*k&amp;65535)&lt;&lt;16)&amp;4294967295,d=d&lt;&lt;15|d&gt;&gt;&gt;17,d=(d&amp;65535)*e+(((d&gt;&gt;&gt;16)*e&amp;65535)&lt;&lt;16)&amp;4294967295,b^=d}b^=a.length;b^=b&gt;&gt;&gt;16;b=2246822507*(b&amp;65535)+((2246822507*(b&gt;&gt;&gt;16)&amp;65535)&lt;&lt;16)&amp;4294967295;b^=b&gt;&gt;&gt;13;b=3266489909*(b&amp;65535)+((3266489909*(b&gt;&gt;&gt;16)&amp;65535)&lt;&lt;16)&amp;4294967295;b^=b&gt;&gt;&gt;16;return b&gt;&gt;&gt;0},hasLocalStorage:function(){try{return!!window.localStorage}catch(a){return!0}},
hasSessionStorage:function(){try{return!!window.sessionStorage}catch(a){return!0}},hasIndexDb:function(){try{return!!window.indexedDB}catch(a){return!0}},isCanvasSupported:function(){var a=document.createElement("canvas");return!(!a.getContext||!a.getContext("2d"))},isIE:function(){return"Microsoft Internet Explorer"===navigator.appName||"Netscape"===navigator.appName&amp;&amp;/Trident/.test(navigator.userAgent)?!0:!1},getPluginsString:function(){return this.isIE()&amp;&amp;this.ie_activex?this.getIEPluginsString():
this.getRegularPluginsString()},getRegularPluginsString:function(){return this.map(navigator.plugins,function(a){var c=this.map(a,function(a){return[a.type,a.suffixes].join("~")}).join(",");return[a.name,a.description,c].join("::")},this).join(";")},getIEPluginsString:function(){if(window.ActiveXObject){var a="ShockwaveFlash.ShockwaveFlash;AcroPDF.PDF;PDF.PdfCtrl;QuickTime.QuickTime;rmocx.RealPlayer G2 Control;rmocx.RealPlayer G2 Control.1;RealPlayer.RealPlayer(tm) ActiveX Control (32-bit);RealVideo.RealVideo(tm) ActiveX Control (32-bit);RealPlayer;SWCtl.SWCtl;WMPlayer.OCX;AgControl.AgControl;Skype.Detection".split(";");
return this.map(a,function(a){try{return new ActiveXObject(a),a}catch(f){return null}}).join(";")}return""},getScreenResolution:function(){var a;return a=this.screen_orientation?screen.height&gt;screen.width?[screen.height,screen.width]:[screen.width,screen.height]:[screen.height,screen.width]},getCanvasFingerprint:function(){var a=document.createElement("canvas"),c=a.getContext("2d"),f="http://valve.github.io";c.textBaseline="top";c.font="14px 'Arial'";c.textBaseline="alphabetic";c.fillStyle="#f60";
c.fillRect(125,1,62,20);c.fillStyle="#069";c.fillText(f,2,15);c.fillStyle="rgba(102, 204, 0, 0.7)";c.fillText(f,4,17);return a.toDataURL()}};return h});dataLayer.push({event:"gtm.fingerprint"});</script><div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div><iframe name="fb_xdm_frame_http" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_http" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="http://staticxx.facebook.com/connect/xd_arbiter/r/XBwzv5Yrm_1.js?version=42#channel=f2251d3f810fccc&amp;origin=http%3A%2F%2Fwww.oddsportal.com" style="border: none;"></iframe><iframe name="fb_xdm_frame_https" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_https" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="https://staticxx.facebook.com/connect/xd_arbiter/r/XBwzv5Yrm_1.js?version=42#channel=f2251d3f810fccc&amp;origin=http%3A%2F%2Fwww.oddsportal.com" style="border: none;"></iframe></div></div><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div></div></div></div><iframe name="oauth2relay236771908" id="oauth2relay236771908" src="https://accounts.google.com/o/oauth2/postmessageRelay?parent=http%3A%2F%2Fwww.oddsportal.com&amp;jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.en_US.vapb4E2BnWs.O%2Fm%3D__features__%2Fam%3DAQ%2Frt%3Dj%2Fd%3D1%2Frs%3DAGLTcCOY6I79W2gOngQhoBDIFvlI0EnkcA#rpctoken=651022108&amp;forcesecure=1" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></body></html>

"""

class Page():

    """
    This contains a page url and all the data on that page
    """

    def __init__(self, url, gamedates):


        self.url = url
        self.gamedates = gamedates

    def __repr__(self):

        return 'Url with {} gamedates'.format(len(self.gamedates))

class GameDate():

    """
    A date and all that games that were played on that day.
    """
    

    def __init__(self, date):

        self.date = date
        self.matches = []

    def __repr__(self):

        return '{} with {} matches'.format(self.date, len(self.matches))

class Match():

    """
    Match info from a game.
    """

    def __init__(self,time, winner, loser,winner_score, loser_score, time2, bs):
        self.time = time
        self.winner= winner
        self.loser= loser
        self.winner_score = winner_score
        self.loser_score= loser_score
        self.time2 = time2
        self.bs = bs 

    def __repr__(self):

        return '{} beat {}'.format(self.winner, self.loser)

    def __str__(self):
        t = self
        return '###'.join([t.time, t.winner, t.loser, t.winner_score, t.loser_score, t.time2, t.bs])



class Collect():

    sleep_time = 10.0
    d = webdriver.Chrome()

    """
    sleep_time
        request timeout
    d
        web driver object. This is literally an instance of chrome. You
        might have to download an extra driver
    """

    def _generate_links(self):

        """
        returns a generator that returns all links in order

        -> generator <string>

        """
        base_str = 'http://www.oddsportal.com/basketball/usa/nba-las-vegas-summer-league-{year}/results/'

        yield from [base_str.format(year = i) for i in range(2013,2017)]

        yield 'http://www.oddsportal.com/basketball/usa/nba-las-vegas-summer-league/results/'

    def _get_tournament_table_html(self, url):

        """
        makes a request to url yielded from generator.
        Returns html source under tournamentTable ID Tag
        """

        html = Collect.d.get(url)
        sleep(Collect.sleep_time)

        return Collect.d.page_source

    def _is_date(self, tr):

        """
        Checks if a specific tag is checking the date or not
        """

        desired_tags = {"center", "nob-border"}

        classes = set(tr.get("class"))

        if not classes:
            return False

        return desired_tags == classes

    def _is_dummy(self,tr):

        classes = set(tr.get("class"))

        d = {'table-dummyrow'}

        return d == classes

    def parse_tr(self, tr):

        time1 = tr.select_one("td.table-time.datet").text
        time2 = tr.select_one("td.center.bold.table-odds.table-score").text
        winner = tr.select_one("td.name.table-participant > a > span").text.strip()
        other = tr.select_one("td.name.table-participant > a").text.replace(winner, "").replace("-", "").strip()
        total = tr.select_one("td.name.table-participant > a").text

        winner_is_zero = total.find(winner) == 0
        scores = tr.select('td.odds-nowrp')
        score1, score2 = scores[0].text, scores[1].text
        bs = tr.select_one("td.center.info-value").text

        if winner_is_zero:

            winner_score = score1
            loser_score = score2
        else:
            winner_score = score2
            loser_score = score1

        return Match(time1, winner,other,time2, winner_score, loser_score, bs)

    def _seperate_by_dates(self, trs):

        game_dates = []

        current_game_date = None

        for tr in trs:

            if self._is_date(tr):
                date_as_text = tr.select_one("> th.first2.tl > span").text
                date_as_obj = parser.parse(date_as_text)
                new_date =  GameDate(date_as_obj)
                game_dates.append(new_date)
                current_game_date = new_date
                continue

            if not current_game_date:
                raise Exception("fuck me")

            match = self.parse_tr(tr)
            current_game_date.matches.append(match)

        t = game_dates[4].matches

        return game_dates

    def _parse_tournament_table_html(self,html,url):

        bs_obj = BeautifulSoup(html, 'lxml')

        tb = bs_obj.select("#tournamentTable > tbody > tr")

        if not tb:
            raise Exception("its empty.")

        _, rest = tb[0], tb[1:]

        remove_dummies = [tr for tr in rest if not self._is_dummy(tr)]

        game_dates = self._seperate_by_dates(remove_dummies)

        return Page(url, game_dates)

    def main(self):

        for url in  self._generate_links():

            
            #html = self._get_tournament_table_html(url)  ### UNCOMMENT ME TO RUN SCRAPER
            html = test ### COMMENT ME OUT
            page_data = self._parse_tournament_table_html(html,url)

            print ("dates")
            
            ### You will have to write data to disk in the format you want 

            print (page_data.gamedates)
            print ("matches")
            print ([x.matches for x in page_data.gamedates])
            break

        # close chrome
        Collect.d.close()

if __name__ == "__main__":
    x = Collect()
    x.main()
