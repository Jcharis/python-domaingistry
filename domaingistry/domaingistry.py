# -*- coding: utf-8 -*-
import json

new_domain = ['app','site','online','xyz','tech','shop','blog','space','live','life','website','news','ninja','solutions','expert','services','media','rocks','company','guru','club','today','agency','technology','tips','center','link','click','ltd','win','work']
common_domain = ['com','edu','net','org','site','co','io','ai','app','ca','uk','ua','us','ru','ch']
extra_domain =["asia","africa","us","me","biz","info","name","mobi","cc","tv","ly","tk","ml","it","to","eu","ch","online"]
prefix_domain = ['a','i','e','the','my','me','we','top','best','get','co','nu','up','new','live','bestof','meta','just','99','101','insta','try','hit','go','re','dr','mr','bit','net','hot','beta','you','our','x','buy','for','pro','ez','on','v','hd','max','digi','free','very','all','easy','cool','air','next','find','uber',]
suffix_domain = ["online.com","world.com","io.com","me.com","you.com","up.com","new.com","blog.com","web.com","hd.com","hq.com","tip.com","tips.com","guru.com","link.com","sumo.com","mob.com","lab.com","labs.com","list.com","info.com","jar.com","egg.com","site.com","app.com","apps.com","net.com","inc.com","247.com","360.com","24x7.com","corp.com","page.com","llc.com","now.com","all.com","box.com","base.com","zone.com","zoom.com","bit.com","bits.com","byte.com","bros.com","cart.com","sale.com","shop.com","store.com","free.com","soft.com","101.com","center.com","pro.com","pros.com","co.com","space.com","hub.com","spot.com","ware.com","talk.com","place.com","kit.com","pad.com","tool.com","bot.com","bots.com","bee.com","doc.com",".com","al.com","ity.com","iput.com","ally.com","ality.com","alness.com","ipital.com"]
sub_domain = ["account","adwords","afp","answers","api","app","bbs","blog","blogsearch","books","checkout","clients","clients1","cloud","code","dashboard","desktop","dev","dl","dns1","dns2","docs","earth","email","feedproxy","finance","forum","ftp","fusion","gmail","groups","host","images","mail","mail1","mail2","mailin1","mailin2","mailserver","manage","maps","mx","mx0","mx01","mx1","mx2","mx7","my","news","ns","ns1","ns2","ns3","ns4","owa","pack","partnerpage","picasa","picasaweb","pop","portal","r.1","r.2","r.3","redbusprimarydns","redbussecondarydns","remote","scholar","secure","secure","server","services","shop","sites","sketchup","smtp","spreadsheets","suggestqueries","support","talkgadget","test","toolbar","translate","video","video-stats.video","vpn","web","webmail","ww1","www"]

# Shuffling Fxn
def shufflize(word):
	new_word = word.split(" ")
	if len(new_word) == 2:
		first_text = new_word[0]
		last_text = new_word[1]
		result = "{}{}".format(last_text,first_text)
	elif len(new_word) == 3:
		first_text = new_word[0]
		mid_text = new_word[1]
		last_text = new_word[2]
		result = "{}{}{}".format(last_text,first_text,mid_text)
	else:
		result = "".join(new_word)
	return result



class Domain(object):
	"""Domain : domain name generation class

	usage
	eg domain = Domain('example','common')
	   domain.generate()

	eg. d2 = Domain(name='jcharis',category='extra')
		d2.get_extra()

	"""
	def __init__(self, name=None,category=None):
		super(Domain, self).__init__()
		self.name = name
		self.category = category

	def __repr__(self):
		return 'Domain(name:{},category:{})'.format(self.name,self.category)

	def generate(self):
		""" Generate A List of Domain Names using the name and the category"""
		new_name = "".join(self.name.lower().split(" "))
		if self.category == 'common':
			result = ['{}.{}'.format(new_name,i)for i in common_domain]
		elif self.category == 'new':
			result = ['{}.{}'.format(new_name,i)for i in new_domain]
		elif self.category == 'extra':
			result = ['{}.{}'.format(new_name,i)for i in extra_domain]
		elif self.category == 'prefix':
			result = ['{}{}.com'.format(i,new_name)for i in prefix_domain]
		elif self.category == 'subdomain':
			result = ['{}.{}.com'.format(i,new_name)for i in sub_domain]
		elif self.category == 'suffix':
			result = ['{}{}'.format(new_name,i)for i in suffix_domain]
		else:
			result = ['{}.{}'.format(new_name,i)for i in common_domain]
		return result


	def get_common(self):
		""" Generate A List of Common Domain Names eg. [com,org,edu]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}.{}'.format(new_name,i)for i in common_domain]
		return result

	def get_new(self):
		""" Generate A List of New Domain Names eg. [ai,app,io]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}.{}'.format(new_name,i)for i in new_domain]
		return result

	def get_extra(self):
		""" Generate A List of Extra Domain Names eg. [shop,tv]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}.{}'.format(new_name,i)for i in extra_domain]
		return result

	def get_prefix(self):
		""" Generate A List of Prefixed Domain Names eg. [topexample.com,thedomain.com]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}{}.com'.format(i,new_name)for i in prefix_domain]
		return result

	def get_subdomain(self):
		""" Generate A List of Prefixed Domain Names eg. [topexample.com,thedomain.com]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}.{}.com'.format(i,new_name)for i in sub_domain]
		return result


	def get_suffix(self):
		""" Generate A List of Suffixed Domain Names eg. [examplify.com,exampletop.com]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}{}'.format(new_name,i)for i in common_domain]
		return result

	def get_shuffled(self):
		""" Generate A List of Shuffled Domain Names eg. [domainname.com,namedomain.com]"""
		result = ['{}.{}'.format(shufflize(self.name.lower()),i) for i in common_domain ]
		return result

	@property 
	def subdomain(self):
		""" Generate A List of Prefixed Domain Names eg. [topexample.com,thedomain.com]"""
		new_name = "".join(self.name.lower().split(" "))
		result = ['{}.{}.com'.format(i,new_name)for i in sub_domain]
		return result


	def to_json(self):
		""" Save A List of All Domain Names to JSON File """
		new_name = "".join(self.name.lower().split(" "))
		new_filename = new_name + '_domain_names' + '.json'
		cust_list_common = ['{}.{}'.format(new_name,i) for i in common_domain ]
		cust_list_new = ['{}.{}'.format(new_name,i) for i in new_domain ]
		cust_list_extra = ['{}.{}'.format(new_name,i) for i in extra_domain ]
		cust_list_prefix = ['{}{}.com'.format(i,new_name) for i in prefix_domain ]
		cust_list_suffix = ['{}{}'.format(new_name,i) for i in suffix_domain ]
		cust_list_subdomain = ['{}.{}.com'.format(i,new_name) for i in sub_domain ]
		cust_list_shuffled = ['{}.{}'.format(shufflize(self.name.lower()),i) for i in common_domain ]
		result = {'common domains':cust_list_common,
		'extra domains':cust_list_extra,
		'new domains':cust_list_new,
		'prefix domains':cust_list_prefix,
		'suffix domains':cust_list_suffix,
		'sub domains':cust_list_subdomain,
		'shuffled_domains':cust_list_shuffled}
		with open(new_filename,"w+") as f:
				f.write(json.dumps(result))
		print('Saved as:: {}'.format(new_filename))






		
		