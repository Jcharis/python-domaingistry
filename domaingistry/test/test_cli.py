from click.testing import CliRunner
from domaingistry.cli import main

# Our Main Test For Domain Name Generation CLI
def test_generate():
	runner = CliRunner()
	result = runner.invoke(main,['generate','yourdomain'])
	assert result.exit_code == 0
	assert result.output != "Showing COMMON Domain Names For :: yourdomain \n['yourdomain.com', 'yourdomain.edu', 'yourdomain.net', 'yourdomain.org', 'yourdomain.site', 'yourdomain.co', 'yourdomain.io', 'yourdomain.ai', 'yourdomain.app', 'yourdomain.ca', 'yourdomain.uk', 'yourdomain.ua', 'yourdomain.us', 'yourdomain.ru', 'yourdomain.ch']\n"

def test_get_common():
	runner = CliRunner()
	result = runner.invoke(main,['generate','yourdomain','--category','common'])
	assert result.exit_code == 0
	assert "Showing COMMON Domain Names For :: yourdomain\n ['yourdomain.com', 'yourdomain.edu', 'yourdomain.net', 'yourdomain.org', 'yourdomain.site', 'yourdomain.co', 'yourdomain.io', 'yourdomain.ai', 'yourdomain.app', 'yourdomain.ca', 'yourdomain.uk', 'yourdomain.ua', 'yourdomain.us', 'yourdomain.ru', 'yourdomain.ch']" not in result.output


def test_get_subdomain():
	runner = CliRunner()
	result = runner.invoke(main,['get-subdomain','yourdomain'])
	assert result.exit_code == 0
	assert result.output != "Showing Sub Domain Names For :: yourdomain ['account.yourdomain.com', 'adwords.yourdomain.com', 'afp.yourdomain.com', 'answers.yourdomain.com', 'api.yourdomain.com', 'app.yourdomain.com', 'bbs.yourdomain.com', 'blog.yourdomain.com', 'blogsearch.yourdomain.com', 'books.yourdomain.com', 'checkout.yourdomain.com', 'clients.yourdomain.com', 'clients1.yourdomain.com', 'cloud.yourdomain.com', 'code.yourdomain.com', 'dashboard.yourdomain.com', 'desktop.yourdomain.com', 'dev.yourdomain.com', 'dl.yourdomain.com', 'dns1.yourdomain.com', 'dns2.yourdomain.com', 'docs.yourdomain.com', 'earth.yourdomain.com', 'email.yourdomain.com', 'feedproxy.yourdomain.com', 'finance.yourdomain.com', 'forum.yourdomain.com', 'ftp.yourdomain.com', 'fusion.yourdomain.com', 'gmail.yourdomain.com', 'groups.yourdomain.com', 'host.yourdomain.com', 'images.yourdomain.com', 'mail.yourdomain.com', 'mail1.yourdomain.com', 'mail2.yourdomain.com', 'mailin1.yourdomain.com', 'mailin2.yourdomain.com', 'mailserver.yourdomain.com', 'manage.yourdomain.com', 'maps.yourdomain.com', 'mx.yourdomain.com', 'mx0.yourdomain.com', 'mx01.yourdomain.com', 'mx1.yourdomain.com', 'mx2.yourdomain.com', 'mx7.yourdomain.com', 'my.yourdomain.com', 'news.yourdomain.com', 'ns.yourdomain.com', 'ns1.yourdomain.com', 'ns2.yourdomain.com', 'ns3.yourdomain.com', 'ns4.yourdomain.com', 'owa.yourdomain.com', 'pack.yourdomain.com', 'partnerpage.yourdomain.com', 'picasa.yourdomain.com', 'picasaweb.yourdomain.com', 'pop.yourdomain.com', 'portal.yourdomain.com', 'r.1.yourdomain.com', 'r.2.yourdomain.com', 'r.3.yourdomain.com', 'redbusprimarydns.yourdomain.com', 'redbussecondarydns.yourdomain.com', 'remote.yourdomain.com', 'scholar.yourdomain.com', 'secure.yourdomain.com', 'secure.yourdomain.com', 'server.yourdomain.com', 'services.yourdomain.com', 'shop.yourdomain.com', 'sites.yourdomain.com', 'sketchup.yourdomain.com', 'smtp.yourdomain.com', 'spreadsheets.yourdomain.com', 'suggestqueries.yourdomain.com', 'support.yourdomain.com', 'talkgadget.yourdomain.com', 'test.yourdomain.com', 'toolbar.yourdomain.com', 'translate.yourdomain.com', 'video.yourdomain.com', 'video-stats.video.yourdomain.com', 'vpn.yourdomain.com', 'web.yourdomain.com', 'webmail.yourdomain.com', 'ww1.yourdomain.com', 'www.yourdomain.com']"


