import sys, argparse, json, requests

import http.client

conn = http.client.HTTPSConnection("api.github.com")
payload = ''

parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True)
parser.add_argument('--token2', required=True)
args = parser.parse_args()
token = args.token
token2 = args.token2

headers_repo = {
	'Authorization': f'token {token}',
	'X-GitHub-Api-Version': '2022-11-28',
	'User-Agent': 'ucupaint-wiki-script' 
}      

def retrieve_contributors(owner:str, repo:str, filename:str):

    conn.request("GET", f"/repos/{owner}/{repo}/contributors", payload, headers_repo)
    res = conn.getresponse()

    # check if response is 200 OK
    if res.status != 200:
        print(f"Error: {res.status} {res.reason}")
        sys.exit(1)
    data = res.read()
    content = data.decode("utf-8")

    # Parse JSON content
    csv_content = ''
    try:
        json_content = json.loads(content)
        for user in json_content:
            if user["type"] == "Bot":
                continue

            csv_content += f"{user['login']}, {user['html_url']}, {user['avatar_url']}\n"
        # print(json.dumps(json_content, indent=2))
    except json.JSONDecodeError:
        print("Failed to parse JSON response:")
        print(content)

    print(csv_content)
    # Save to file
    with open(filename, 'w') as f:
        f.write(csv_content)

API_URL = "https://api.github.com/graphql"
headers_sponsor = {"Authorization": f"bearer {token2}"}

QUERY = """
{
  viewer {
    login
    ... on Sponsorable {
      sponsors(first: 100, orderBy: {field: RELEVANCE, direction: DESC}) {
        totalCount
        pageInfo { hasNextPage endCursor }
        nodes {
          __typename
          ... on User {
            login
            name
            url
            avatarUrl
            sponsorshipForViewerAsSponsorable {
              isActive
              createdAt
              tier {
                id
                name
                isOneTime
                monthlyPriceInDollars
              }
            }
          }
          ... on Organization {
            login
            name
            description
            avatarUrl
            twitterUsername
            sponsorshipForViewerAsSponsorable {
              isActive
              createdAt
              tier {
                id
                name
                isOneTime
                monthlyPriceInDollars
              }
            }
          }
        }
      }
    }
    sponsorsListing {
      url
      fullDescription
      activeGoal {
        kind
        description
        percentComplete
        targetValue
        title
      }
      tiers(first: 100) {
        nodes {
          id
          name
          isOneTime
          description
          monthlyPriceInDollars
          isCustomAmount
        }
      }
    }
  }
}
"""

def fetch_public_sponsors(login: str, page_size: int = 100):
    sponsors = []
    goal = None
    after = None

    variables = {"login": login, "first": page_size, "after": after}
    resp = requests.post(API_URL, json={"query": QUERY, "variables": variables}, headers=headers_sponsor)
    resp.raise_for_status()
    data = resp.json()

    print(json.dumps(data, indent=2))
 
    listing = data["data"]["viewer"]["sponsorsListing"]
    if listing:
        if listing.get("activeGoal"):
            goal = listing["activeGoal"]
            goal["url"] = listing.get("url")
            goal["fullDescription"] = listing.get("fullDescription")

        
        if listing.get("tiers"):
            all_tiers = listing["tiers"]["nodes"]
            selected_tiers = []
            for t in all_tiers:
                if not t.get("isOneTime"):
                    trim_name = t.get("description")

                    # only keep first line of description
                    if trim_name:
                        trim_name = trim_name.split('\n')[0]
                        # trim first 4 chars
                        if len(trim_name) > 4:
                            trim_name = trim_name[4:]
                    new_tier = {
                        "name": trim_name,
                        "price": t.get("monthlyPriceInDollars"),
                        "description": t.get("description"),
                    }
                    selected_tiers.append(new_tier)
            if selected_tiers:
                goal["tiers"] = selected_tiers

    tiers = goal.get("tiers") if goal else None
    while True:
        conn = data["data"]["viewer"]["sponsors"]
        for node in conn["nodes"]:
            sponsorship = node.get("sponsorshipForViewerAsSponsorable")
            tier = sponsorship.get("tier") if sponsorship else None

            new_sp = {
                "login": node.get("login"),
                "profile": node.get("url"),
                "avatar_url": node.get("avatarUrl"),
                "tier": 0,

                "price_usd": tier["monthlyPriceInDollars"] if tier else None,
                "is_one_time": tier["isOneTime"] if tier else None,
                "since": sponsorship["createdAt"],
            }
            if tiers:
                for i, t in enumerate(tiers):
                    if new_sp["price_usd"] <= t["price"]:
                        new_sp["tier"] = i
                        break
            sponsors.append(new_sp)
        if conn["pageInfo"]["hasNextPage"]:
            after = conn["pageInfo"]["endCursor"]
        else:
            break
        
    return sponsors, goal

def sponsor_sort_key(s):
    # sort by is_one_time (False first), price_usd (desc), since (asc)
    # return (s["is_one_time"], -(s["price_usd"] or 0), s["since"])
    return (-(s["price_usd"] or 0), s["since"])

def retrieve_sponsors(owner:str, filename:str):
    sponsors, goal = fetch_public_sponsors(owner)
    sponsors.sort(key=sponsor_sort_key)

    csv_content = ''

    for s in sponsors:
       csv_content += f"{s['login']}, {s['profile']}, {s['avatar_url']}, {s['since']}, {s['price_usd']}, {s['is_one_time']}, {s['tier']}\n"

    print(csv_content)
    with open(filename, 'w') as f:
        f.write(csv_content)

    if goal:
        print(json.dumps(goal, indent=2))
        with open('sponsorship-goal.json', 'w') as f:
            json.dump(goal, f, indent=2)

retrieve_contributors('ucupumar', 'ucupaint', 'contributors.csv')
retrieve_contributors('ucupumar', 'ucupaint-wiki', 'contributors-wiki.csv')
retrieve_sponsors('ucupumar', 'sponsors.csv')