import discord
import requests

from discord.ext import commands

class Github(commands.Cog):
	"""Github statistics commands"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def ghuserinfo(self, ctx, *, user):
		"""
		Shows info about a user in github
		Example:
			[p]ghuserinfo kyb3r
		"""
		r = requests.get(f"https://api.github.com/users/{user}")
		r = r.json()
		title = r["login"]
		url = r["html_url"]
		image = r["avatar_url"]
		org = r["company"]
		site = r["blog"]
		hireable = r["hireable"]
		bio = r["bio"]
		repos = r["public_repos"]
		gists = r["public_gists"]
		followers = r["followers"]
		following = r["following"]
		created = r["created_at"]
		updated = r["updated_at"]
		embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
		embed.add_field(name="Bio", value=bio)
		embed.add_field(name="Website", value=site)
		embed.add_field(name="Company",  value=org)
		embed.add_field(name="Hireable", value=hireable)
		embed.add_field(name="Repositories(public)", value=repos)
		embed.add_field(name="Gists(public)", value=gists)
		embed.add_field(name="Followers", value=followers)
		embed.add_field(name="Following", value=following)
		embed.add_field(name="Created", value=created)
		embed.set_thumbnail(url=image)
		embed.set_footer(text=f"{title} latestly updated his/her profile on {updated}")
		await ctx.send(embed=embed)
		
	@commands.command()
	async def orginfo(self, ctx, *, org):
		"""
		Shows info about the organization of github
		Example:
			[p]orginfo heroku
		"""
		r = requests.get(f"https://api.github.com/orgs/{org}")
		r = r.json()
		name = r["name"]
		id = r["id"]
		url = r["html_url"]
		avatar = r["avatar_url"]
		desc = r["description"]
		website = r["blog"]
		location = r["location"]
		repos = r["public_repos"]
		gists = r["public_gists"]
		created = r["created_at"]
		
		embed = discord.Embed(title=name, url=url, description=desc, color=discord.Color.blurple())
		embed.set_thumbnail(url=avatar)
		embed.add_field(name="ID", value=id, inline=True)
		embed.add_field(name="Location", value=location, inline=True)
		embed.add_field(name="Website", value=website, inline=True)
		embed.add_field(name="Repositories", value=repos, inline=True)
		embed.add_field(name="Gists", value=gists, inline=True)
		embed.add_field(name="Created", value=created)
		await ctx.send(embed=embed)
		
	@commands.command()
	async def repoinfo(self, ctx, repoowner, *, reponame):
		"""
		Shows the info about repo
		Example:
			[p]repoinfo kyb3r modmail
		"""
		r = requests.get(f"https://api.github.com/repos/{repoowner}/{reponame}")
		r = r.json()
		tname = r["full_name"]
		url = r["html_url"]
		owner = r["owner"]["login"]
		desc = r["description"]
		created = r["created_at"]
		updated = r["updated_at"]
		giturl = r["git_url"]
		size = r["size"]
		lang = r["language"]
		issues = r["open_issues_count"]
		liscense = r["license"]["name"]
		forks = r["forks"]
		stars = r["stargazers_count"]
		subscriber = r["subscribers_count"]
		embed = discord.Embed(color=discord.Color.blurple(), description=desc, url=url, title=tname)
		embed.add_field(name="Owner", value=owner)
		embed.add_field(name="Language", value=lang)
		embed.add_field(name="Size", value=size)
		embed.add_field(name="Git-Url", value=giturl)
		embed.add_field(name="Issues(open)", value=issues)
		embed.add_field(name="Forks", value=forks)
		embed.add_field(name="Watchs", value=subscriber)
		embed.add_field(name="Stars", value=stars)
		embed.add_field(name="License", value=liscense)
		embed.set_footer(text=f"{tname} created on {created} and latestly updated on {updated}")
		await ctx.send(embed=embed)
			
	@commands.command()
	async def commitinfo(self, ctx, repoowner, reponame, *, commitsha):
		"""
		Shows the info about commit
		Example usage:
			[p]commitinfo kyb3r modmail ca0b61d943168a585e2972c112ea13871773e792
		"""
		r = requests.get(f"https://api.github.com/repos/{repoowner}/{reponame}/commits/{commitsha}")
		r = r.json()
		url = r["html_url"]
		author = r["author"]["login"]
		commiter = r["commiter"]["login"]
		parents = r["parents"]["html_url"]
		adds = r["stats"]["additions"]
		dels = r["stats"]["deletions"]
		total = adds + dels
		embed = discord.Embed(color=discord.Color.blurple())
		embed.add_field(name="Commit URL", value=url)
		embed.add_field(name="Author", value=author)
		embed.add_field(name="Commiter", value=commiter)
		embed.add_field(name="Parents", value=parents)
		embed.add_field(name="Stats", value=f"Total - {total}\nAdditions - {adds}\nDeletions - {dels}")
		await ctx.send(embed=embed)
		
	@commands.command()
	async def issueinfo(self, ctx, repoowner, reponame, *, issuenum):
		"""
		Shows info about a issue
		Exampe:
			[p]issueinfo kyb3r modmail 2762
		"""
		r = requests.get(f"https://api.github.com/repos/{repoowner}/{reponame}/issues/{issuenum}")
		r = r.json()
		title = r["title"]
		url = r["html_url"]
		openedby = r["user"]["login"]
		labels = r["labels"]
		state = r["state"]
		asignees = r["assignees"]
		comments = r["comments"]
		created = r["created_at"]
		body = r["body"]
		embed = discord.Embed(color=discord.Color.blurple(), title=title, url=url)
		embed.add_field(name="Opened", value=openedby)
		embed.add_field(name="Labels", value=labels)
		embed.add_field(name="State", value=state)
		embed.add_field(name="Opened-on", value=created)
		embed.add_field(name="Asignees", value=asignees)
		embed.add_field(name="Comments", value=comments)
		embed.add_field(name="Body", value=body)
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(Github(bot))
