from webscraper import start_scraper

# ----- MESSAGE ------
message = fr"""
{'-'*70}

__          ________ _      _____ ____  __  __ ______ 
\ \        / /  ____| |    / ____/ __ \|  \/  |  ____|
 \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   
  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  
   \  /\  /  | |____| |___| |___| |__| | |  | | |____ 
    \/  \/   |______|______\_____\____/|_|  |_|______|
                                                      
This is a simple Web scraper that scrapes the news website
                quantamagazine.org

{'-'*70}
"""

print(message)


# ----- INPUTS ------
while True:
	print("Input how many pages you want articles from. The more pages, the longer it takes (Can't enter 0 or below)\n")

	while True:
		pages = int(input("Pages: "))
		if pages <= 0:
			print("Enter again.\n")
			continue
		else:
			break


	print("""\n
Enter the sections you want in the list one by one. you can use multiple sections or just one. Use the keywords as given below.
Capitals and wrong spellings exit the loop

Keywords:
	physics
	mathematics
	biology
	computer-science
	archive (EVERYTHING, instantly breaks out of loop)

press enter again or anything else to exit loop\n
	""")
	sections=[]
	while True:
		print(f"List so far: {sections}")
		section = input("Enter section keyword: ")
		if section in ("physics", "mathematics", "biology", "computer-science"):
			sections.append(section)
			continue
		elif section == "archive":
			sections.clear()
			sections.append(section)
			break
		else:
			break

	print("LOADING LIST...\n")

	# ----- SCRAPER -----
	try:
		start_scraper(pages, sections)
		print("\n Done!")

		res = ("""
			Do you want to restart? (y/n)
			""")
		if res in ("y", "Y"):
			continue
		else:
			break
		
	except:
		res1 = ("""
			Something went wrong...
			Do you want to restart? (y/n)
			""")
		if res1 in ("y", "Y"):
			continue
		else:
			break



