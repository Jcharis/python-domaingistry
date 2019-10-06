#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from click_didyoumean import DYMGroup
import json,pprint

new_domain = ['app','site','online','xyz','tech','ai','shop','blog','space','live','life','website','news','ninja','solutions','expert','services','media','rocks','company','guru','club','today','agency','technology','tips','center','link','click','ltd','win','work']

common_domain = ['com','edu','net','org','site','co','io','ai','app','ca','uk','ua','us','ru','ch']

extra_domain =["asia","africa","us","me","biz","info","name","mobi","cc","tv","ly","it","to","eu","ch","online"]

prefix_domain = ['a','i','e','the','my','me','we','top','best','get','co','nu','up','new','live','bestof','meta','just','99','101','insta','try','hit','go','re','dr','mr','bit','net','hot','beta','you','our','x','buy','for','pro','ez','on','v','hd','max','digi','free','very','all','easy','cool','air','next','find','uber',]

suffix_domain = ["online.com","world.com","io.com","me.com","you.com","up.com","new.com","blog.com","web.com","hd.com","hq.com","tip.com","tips.com","guru.com","link.com","sumo.com","mob.com","lab.com","labs.com","list.com","info.com","jar.com","egg.com","site.com","app.com","apps.com","net.com","inc.com","247.com","360.com","24x7.com","corp.com","page.com","llc.com","now.com","all.com","box.com","base.com","zone.com","zoom.com","bit.com","bits.com","byte.com","bros.com","cart.com","sale.com","shop.com","store.com","free.com","soft.com","101.com","center.com","pro.com","pros.com","co.com","space.com","hub.com","spot.com","ware.com","talk.com","place.com","kit.com","pad.com","tool.com","bot.com","bots.com","bee.com","doc.com",".com","al.com","ity.com","iput.com","ally.com","ality.com","alness.com","ipital.com"]

sub_domain = ["account","adwords","afp","answers","api","app","bbs","blog","blogsearch","books","checkout","clients","clients1","cloud","code","dashboard","desktop","dev","dl","dns1","dns2","docs","earth","email","feedproxy","finance","forum","ftp","fusion","gmail","groups","host","images","mail","mail1","mail2","mailin1","mailin2","mailserver","manage","maps","mx","mx0","mx01","mx1","mx2","mx7","my","news","ns","ns1","ns2","ns3","ns4","owa","pack","partnerpage","picasa","picasaweb","pop","portal","r.1","r.2","r.3","redbusprimarydns","redbussecondarydns","remote","scholar","secure","secure","server","services","shop","sites","sketchup","smtp","spreadsheets","suggestqueries","support","talkgadget","test","toolbar","translate","video","video-stats.video","vpn","web","webmail","ww1","www"]


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
		
		

		

@click.group(cls=DYMGroup)
@click.version_option(version='0.0.2',prog_name='domain-gistry')
def main():
	""" Domain-Gistry : A Domain Name Generation CLI
		
	"""
	pass


@main.command()
@click.argument('name')
@click.option('--category','-c',help='Specify Category of Domain Names Extension [new|common|extra|suffix|prefix|all]',default='common')
@click.option('--save','-s',help='Save Results to Txt file [yes|no]',default='no')
def generate(name,category,save):
	""" Generate Domain Names

	eg. domain-gistry generate yourdomain 

	eg. domain-gistry generate yourdomain --category common --save yes

	eg. domain-gistry generate yourdomain -c common 
	
	eg. domain-gistry generate "your domain"

	eg. python domain-gistry.py generate yourdomain


	"""
	click.secho("Showing {} Domain Names For :: {}".format(category.upper(),name),fg='white',bg='blue')

	raw_name = "".join(name.lower().split(" "))
	if save == 'yes':
		filename = raw_name + '_domain_names' + '.txt'
		click.secho('Saved Results To :: {}'.format(filename),fg='white',bg='red')
		if category == 'new':
			cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
			result = cust_list_new
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'common':
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			result =cust_list_common
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'extra':
			cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
			result = cust_list_extra
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'prefix':
			cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
			result = cust_list_prefix
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'subdomain':
			cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
			result = cust_list_subdomain
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'suffix':
			cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
			result = cust_list_suffix
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'shuffled':
			cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
			result = cust_list_shuffled
			with open(filename,"w+") as f:
				f.write(json.dumps(result))
		elif category == 'all':
			new_filename = raw_name + '_domain_names' + '.json'
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
			cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
			cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
			cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
			cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
			cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
			non_prettified_result = {'common domains':cust_list_common,
			'extra domains':cust_list_extra,
			'new domains':cust_list_new,
			'prefix domains':cust_list_prefix,
			'suffix domains':cust_list_suffix,
			'sub domains':cust_list_subdomain,
			'shuffled_domains':cust_list_shuffled}
			result = pprint.pprint(non_prettified_result)
			with open(new_filename,"w+") as f:
				f.write(json.dumps(non_prettified_result))

		else:
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			result = cust_list_common
			with open(filename,"w+") as f:
				f.write(result)

	else:
		if category == 'new':
			cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
			result = cust_list_new
		elif category == 'common':
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			result =cust_list_common
		elif category == 'extra':
			cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
			result = cust_list_extra
		elif category == 'prefix':
			cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
			result = cust_list_prefix
		elif category == 'subdomain':
			cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
			result = cust_list_subdomain
		elif category == 'suffix':
			cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
			result = cust_list_suffix
		elif category == 'shuffled':
			cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
			result = cust_list_shuffled
		elif category == 'all':
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
			cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
			cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
			cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
			cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
			cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
			non_prettified_result = {'common domains':cust_list_common,
			'extra domains':cust_list_extra,
			'new domains':cust_list_new,
			'prefix domains':cust_list_prefix,
			'sub domains':cust_list_subdomain,
			'suffix domains':cust_list_suffix,
			'shuffled_domains':cust_list_shuffled}
			result = pprint.pprint(non_prettified_result)

		else:
			cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
			result = cust_list_common
	return click.echo(result)


@main.command()
@click.argument('name')
def get_common(name):
	""" Get Common Domain Names [com,org,edu.co]

	eg. domain-gistry get-common example

	eg. domain-gistry get-common example

	"""
	click.secho("Showing Common Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
	click.echo(cust_list_common)
	

@main.command()
@click.argument('name')
def get_extra(name):
	""" Get Extra Domain Names [tv,mobile,app]

	eg. domain-gistry get-extra example

	eg. domain-gistry get-extra example

	"""
	click.secho("Showing Extra Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
	click.echo(cust_list_extra)


@main.command()
@click.argument('name')
def get_new(name):
	""" Get New Domain Names [ai,io]

	eg. domain-gistry get-new example

	eg. domain-gistry get-new example

	"""
	click.secho("Showing New Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
	click.echo(cust_list_new)

@main.command()
@click.argument('name')
def get_prefix(name):
	""" Get Prefixed Domain Names [topexample.com,theexample.com]

	eg. domain-gistry get-prefix example

	eg. domain-gistry get-prefix example

	"""
	click.secho("Showing Prefixed Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
	click.echo(cust_list_prefix)


@main.command()
@click.argument('name')
def get_suffix(name):
	""" Get Suffixed Domain Names [exampletop.com,examplify.com]

	eg. domain-gistry get-suffix example

	eg. domain-gistry get-suffix example
	
	"""
	click.secho("Showing Suffixed Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
	click.echo(cust_list_suffix)

@main.command()
@click.argument('name')
def get_subdomain(name):
	""" Get Sub Domain Names [blog.example.com,app.example.com]

	eg. domain-gistry get-subdomain example

	eg. domain-gistry get-subdomain example

	"""
	click.secho("Showing Sub-Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
	click.echo(cust_list_subdomain)


@main.command()
@click.argument('name')
def get_shuffled(name):
	""" Get Shuffled Domain Names (usually more than one term) [exampletop.com,topexample.com]

	eg. domain-gistry get-shuffled "top example"

	eg. domain-gistry get-shuffled "top example"
	
	"""
	click.secho("Showing Suffixed Domain Names For :: {}".format(name),fg='white',bg='blue')
	cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
	click.echo(cust_list_shuffled)

@main.command()
@click.argument('name')
@click.option('--save','-s',help='Save All Results to JSON File',default='no')
def get_all(name,save):
	""" Get all Domain Names 

	eg. domain-gistry get-all example

	eg. domain-gistry get-all example

	"""
	click.secho("Showing All Domain Names For :: {}".format(name),fg='white',bg='blue')
	raw_name = "".join(name.lower().split(" "))
	if save == 'yes':
		filename = raw_name + '_domain_names' + '.json'
		cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
		cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
		cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
		cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
		cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
		cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
		cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
		all_list = {'common domains':cust_list_common,
		 'extra domains':cust_list_extra,
		 'new domains':cust_list_new,
		 'prefix domains':cust_list_prefix,
		 'sub domains':cust_list_subdomain,
		 'suffix domains':cust_list_suffix,
		 'shuffled_domains':cust_list_shuffled}
		with open(filename,"w+") as f:
			f.write(json.dumps(all_list))
		click.echo(json.dumps(all_list,indent=4, sort_keys=True))
		click.secho('Saved Results to File {}'.format(filename),fg='white',bg='green')
	else:
		cust_list_common = ['{}.{}'.format(raw_name,i) for i in common_domain ]
		cust_list_new = ['{}.{}'.format(raw_name,i) for i in new_domain ]
		cust_list_extra = ['{}.{}'.format(raw_name,i) for i in extra_domain ]
		cust_list_prefix = ['{}{}.com'.format(i,raw_name) for i in prefix_domain ]
		cust_list_suffix = ['{}{}'.format(raw_name,i) for i in suffix_domain ]
		cust_list_subdomain = ['{}.{}.com'.format(i,raw_name) for i in sub_domain ]
		cust_list_shuffled = ['{}.{}'.format(shufflize(name),i) for i in common_domain ]
		all_list = {'common domains':cust_list_common,
		 'extra domains':cust_list_extra,
		 'new domains':cust_list_new,
		 'prefix domains':cust_list_prefix,
		 'suffix domains':cust_list_suffix,
		 'sub domains':cust_list_subdomain,
		 'shuffled_domains':cust_list_shuffled}
		click.echo(json.dumps(all_list,indent=4, sort_keys=True))

@main.command()
def info():
	""" Show Info About Software 
	
	eg. domain-gistry info

	eg domain-gistry info

	"""


	click.secho('Name:: {}'.format('DomainGistry-CLI'),bg='red')
	click.secho('Version:: {}'.format('0.0.2'),bg='yellow')
	click.secho('Motto:: {}'.format('Jesus Saves@JCharisTech'),bg='green')
	click.secho('Author:: {}'.format('Jesse E Agbe(JCharis)'),bg='blue')


if __name__ == '__main__':
	main()