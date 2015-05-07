var min = timestamp('January 2006');
var max = timestamp('2015');
var alternate = 0;

function timeline_init(){
	datePicker = document.getElementById("datePicker");
	datePicker.setAttribute("max", max);
	datePicker.setAttribute("min", min);
	datePicker.setAttribute("value", timestamp('July 2010'));
	changeDate(datePicker.getAttribute("value"));

	addTimepieces();
}

function addTimepieces(){
	addTimepiece("Judge Rules NYPD Stop-and-Frisk Unconstitutional", 
		"Judge Shira Scheindlin issues her long-awaited opinion finding that the New York City Police Department had violated the Fourth and Fourteenth Amendments in the way they have conducted stop and frisks.", 
		"http://www.wnyc.org/articles/wnyc-news/2013/aug/12/stop-and-frisk-decision-comes-down/", 
		"Aug 12, 2013");
	addTimepiece("NYPD Agrees to Erase Names in Stop and Frisk Database", 
		"According to a settlement reached between the city and the New York Civil Liberties Union, the New York Police Department must erase the hundreds of thousands of names and addresses it collected during stops and frisks.", 
		"http://www.wnyc.org/articles/wnyc-news/2013/aug/07/nypd-erase-all-names-stop-and-frisk-database/", 
		"Aug 7, 2013");
	addTimepiece("Council Passes Sweeping Plan for NYPD Oversight", 
		"The City Council passed with a veto-proof majority an expansive plan that imposed increased oversight on the NYPD and made it easier for people to bring profiling claims against the police.", 
		"http://www.wnyc.org/articles/wnyc-news/2013/jun/27/council-passes-sweeping-plan-nypd-oversight/", 
		"June 27, 2013");
	addTimepiece("Closing Arguments End in Stop and Frisk Trial", 
		"Lawyers complete their closing arguments in a federal case challenging the way the NYPD has been conducting the practice of stop and frisk.", 
		"http://www.wnyc.org/articles/wnyc-news/2013/may/20/closing-arguments-underway-stop-and-frisk-trial/", 
		"May 20, 2013")
	addTimepiece("See Where Stop-and-Frisks Fell (and Rose) in 2012", 
		"The city has released annual data on every stop-and-frisk in 2012, revealing a 22 percent decline in stops, overall. WNYC mapped out where exactly the number of stops increased and decreased.", 
		"http://www.wnyc.org/articles/wnyc-news/2013/apr/22/stop-and-frisk-focus/", 
		"April 22, 2013");
	addTimepiece("Federal Class Action Against NYPD Stops to Begin", 
		"A federal, class action suit challenges the practice of stop-and-frisk on the basis it is unconstitutional, posing the most comprehensive legal challenge to the tactic yet.",
		"http://www.wnyc.org/articles/wnyc-news/2013/mar/17/federal-class-action-against-nypd-stops-begin/",
		"March 17, 2013");
	addTimepiece("Critics Challenge NYPD Clean Halls Program in Court", 
		"Civil rights groups began making their case in U.S. District Court to limit a citywide policy that allows the police department to patrol more than 10,000 private buildings.",
		"http://www.wnyc.org/articles/wnyc-news/2012/oct/15/blog-clean-halls/",
		"Oct 15, 2012");
	addTimepiece("Bloomberg Say Bronx DA Should Review Policy Change", 
		"Mayor Michael Bloomberg came out against the Bronx district attorney's decision to limit stop-and-frisk prosecutions, saying, “If you want to bring crime back to New York, this is probably a good way to do it.”",
		"http://www.wnyc.org/articles/wnyc-news/2012/sep/27/blog-bloomberg-say-bronx-da-should-review-policy-change/",
		"Sept 27, 2012");
	addTimepiece("Bronx DA No Longer Prosecuting Some Stop-And-Frisk Cases",
		"The Bronx district attorney's office says that it will no longer prosecuting people stopped and arrested for trespassing unless the arresting officer ensures the arrest is warranted.",
		"http://www.wnyc.org/articles/wnyc-news/2012/sep/26/blog-bronx-da-no-longer-prosecutes-some-stop-and-frisk-cases/",
		"Sept 26, 2012");
	addTimepiece("NY Court Reverses Stop and Frisk Conviction",
		"A New York appeals court reversed the conviction of a 14-year-old-boy who had been arrested after a street search found a weapon in his backpack, ruling that the officers lacked the reasonable suspicion required to justify the search.",
		"http://www.wnyc.org/articles/wnyc-news/2012/jul/03/ny-court-reverses-stop-and-frisk-conviction/",
		"July 3, 2012");
	addTimepiece("Council Members Propose NYPD Oversight Amid Criticism",
		"About two dozen City Council members propose legislation that would create an inspector general to monitor the NYPD",
		"http://www.wnyc.org/articles/wnyc-news/2012/jun/13/blog-council-members-propose-nypd-oversight/",
		"June 13, 2012");
	addTimepiece("Bloomberg Defends NYPD Practices",
		"Mayor Michael Bloomberg defended stop and frisk practices and said the NYPD will continue the practice that has faced increasing scrutiny.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2012/may/18/bloomberg-says-nypd-isnt-walking-away-stop-and-frisk/",
		"May 20, 2012");
	addTimepiece("Kelly Outlines Changes",
		"Commissioner Kelly sent a letter to Speaker Christine Quinn outlining changes to the NYPD's stop-and-frisk policy, including changes to training and supervision.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2012/may/17/nypd-planning-changes-stop-and-frisk-policy/",
		"May 17, 2012");
	addTimepiece("Class-action Status Granted",
		"A federal judge grants class action status to a lawsuit accusing the NYPD of discriminating against blacks and Latinos with its stop-and-frisk policy.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2012/may/17/nypds-stop-and-frisk-policy-faces-class-action-suit/",
		"May 16, 2012");
	addTimepiece("Livery Cab Lawsuit Settled",
		"The city settled the federal lawsuit that challenged the NYPD's stop-and-frisk livery cab passengers.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2012/may/15/city-settles-livery-cab-frisk-lawsuit/",
		"May 15, 2012");
	addTimepiece("NYPD Orders Commanders to Review Reports",
		"The NYPD orders commanders to review stop-and-frisk activity. High-level police officials are instructed to review of stop-and-frisk reports to ensure they are proper, and not an effort to meet productivity goals.",
		"http://www.wnyc.org/articles/wnyc-news/2012/may/09/nypd-ordered-review-stop-and-frisk-activity/",
		"May 9, 2012");
	addTimepiece("Reform Package Introduced",
		"The City Council introduces a package of police reform bills to bring greater accountability to the NYPD, in particular the NYPD's stop-and-frisk practices.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2012/feb/29/council-members-tout-legislation-aimed-nypd-accountability/",
		"Feb 29, 2012");
	addTimepiece("Legislation Proposed for Independent Watchdog",
		"Brooklyn area state legislators introduce legislation that would establish an NYPD independent inspector general position. The call for such a move comes from NYPD surveillance of the Muslim community and stop-and-frisk.",
		"http://www.wnyc.org/blogs/empire/2012/feb/10/brooklyn-state-legislators-introduce-nypd-oversight-legislation/",
		"Feb 10, 2012");
	addTimepiece("Class Action Motion Filed", 
		"Plaintiffs in CCR case file motion for Class Certification",
		"#",
		"Nov 7, 2011");
	addTimepiece("Politicians Call for Federal Probe",
		"Some NYC politicians call for a federal probe of the NYPD's stop-and-frisk policy.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2011/oct/19/stop_and_frisk/",
		"Oct 19, 2011")
	addTimepiece("Councilman Stopped and Detained",
		"A day after being stopped and detained by the NYPD, City Councilman Jumaane Williams and others urge for reforms to the stop-and-frisk policy.",
		"http://www.wnyc.org/blogs/empire/2011/sep/06/councilmans-police-detainment-could-give-push-to-stop-and-frisk-challenges/",
		"Sep 6, 2011");
	addTimepiece("Suit Filed Over Stops of Livery Car Passengers",
		"The NYCLU files a federal lawsuit against the NYPD and NYC for stop-and-frisk of passengers in livery cars.",
		"http://www.wnyc.org/blogs/wnyc-news-blog/2011/may/26/lawsuit-alleges-illegal-stop-and-frisks-livery-car-passengers/",
		"May 26, 2011");
	addTimepiece("Paterson Changes Policy",
		"Gov. Paterson Changes the NYPD's Stop-and-Frisk Policy. It doesn't stop the policy, but it does prevent the NYPD from keeping data about people who have not committed any crime.",
		"http://www.wnyc.org/articles/wnyc-news/2010/jul/16/paterson-changes-nypds-stop-and-frisk-policy/",
		"July 16, 2010");
	addTimepiece("Suit Seeks to Erase Record of People Stopped and Not Arrested",
		"Another lawsuit, this time filed by the New York Civil Liberties Union, seeks to stop the city from keeping a huge database of New Yorkers stopped, but never charged.",
		"http://www.wnyc.org/articles/wnyc-news/2010/may/19/new-lawsuit-challenges-stop-and-frisk-policy_/",
		"May 19, 2010");
	addTimepiece("Issue in Mayoral Race",
		"Stop-and-Frisk become an issue in the mayoral race, as well as the Manhattan DA's race.",
		"http://www.wnyc.org/articles/wnyc-news/2009/sep/05/stop-and-frisk-becomes-issue-in-mayors-race/",
		"Sept, 2009");
	addTimepiece("NYCLU predicts record year for stop-and-frisks",
		"The New York Civil Liberties Union says the NYPD is on pace to break last year's record for stop and frisk encounters. In the first half of 2009, the NYPD made 311,000 stops.",
		"http://www.wnyc.org/articles/wnyc-news/2009/aug/14/nyclu-says-stop-and-frisks-increasing/",
		"Aug 14, 2009");
	addTimepiece("Analysis Suggests Racial Profiling",
		"A new analysis of NYPD stop-and-frisk data prompts critics to raise new questions about the tactic's effectiveness.",
		"http://www.wnyc.org/articles/wnyc-news/2009/may/01/analysis-suggests-racial-profiling-in-nypd-stop-and-frisk/",
		"May 1, 2009");
	addTimepiece("10 Year of Data Ordered Opened",
		"Judge orders the city and the NYPD to turn over all UF-250 (stop-and-frisk) data for the past 10 years.",
		"#",
		"Sep 10, 2008");
	addTimepiece("NYPD Ordered to Turn Over Stop-and-Frisk Data",
		"The NYPD is ordered to turn over stop-and-frisk data to the NYCLU.",
		"http://www.wnyc.org/articles/wnyc-news/2008/may/30/nypd-ordered-to-turn-over-stop-and-frisk-data-to-nyclu/",
		"May 30, 2008");
	addTimepiece("Data Sought to 1998",
		"The Center for Constitutional Rights amends its initial complaint to seek class-action status in Floyd v. City of New York. A few days later they seek stop-and-frisk data going back to 1998.",
		"#",
		"April 15, 2008");
	addTimepiece("RAND Study:No Racial Profiling",
		"A RAND study finds the NYPD's stop-and-frisk program did not engage in racial profiling.",
		"http://www.wnyc.org/articles/wnyc-news/2007/nov/20/report-defends-nypds-controversial-tactics/",
		"Nov 20, 2007");
	addTimepiece("Quinn: NYPD Not Releasing All Data",
		"City Council Speaker Christine Quinn says the NYPD isn't meeting its legal obligation to publicly release all its stop-and-frisk data.",
		"http://www.wnyc.org/articles/wnyc-news/2007/jul/28/quinn-wants-nypd-to-release-stop-and-frisk-data/",
		"July 28, 2007");
	addTimepiece("Sharpton Threatens Lawsuit",
		"Angered by stop-and-frisk statistics, Al Sharpton says he'll initiate a suit against the NYPD.",
		"http://www.wnyc.org/articles/wnyc-news/2007/feb/05/sharpton-starts-class-action-suit-against-nypd/",
		"Feb 5, 2007");
	
}

function addTimepiece(title, text, link, date){
	var timepieces = document.getElementById("timepieces");

	var tooltip = document.createElement("a");
	tooltip.setAttribute("href", link);
	tooltip.setAttribute("class", "tooltip");

	var timepiece = document.createElement("div");
	timepiece.setAttribute("class", "timepiece");

	var callout = document.createElement("span");

	var calloutimg = document.createElement("img");
	calloutimg.setAttribute("class", "callout");
	calloutimg.setAttribute("src", "../static/img/callout.gif");

	var titleStrong = document.createElement("strong");
	var titleText = document.createTextNode(title);
	titleStrong.appendChild(titleText);

	var textNode = document.createTextNode(text + " ["+date+"]");

	callout.appendChild(calloutimg);
	callout.appendChild(titleStrong);
	callout.appendChild(document.createElement("br"));
	callout.appendChild(textNode);

	tooltip.appendChild(timepiece);
	tooltip.appendChild(callout);
	timepieces.appendChild(tooltip);

	var time = timestamp(date);

	var loc = (time-min)/(max-min)*($("#timeline").width()) + 'px';

	//alert(loc)

	tooltip.style.left = loc;
	if(alternate == 0){
		tooltip.style.top = "80px";
	}else if (alternate == 1){
		tooltip.style.top = "65px";
	}else if (alternate == 2){
		tooltip.style.top = "50px";
	}else{
		tooltip.style.top = "65px";
	}
	alternate = (alternate + 1)%4;
}

// Create a list of day and monthnames.
var
	weekdays = [
		"Sunday", "Monday", "Tuesday",
		"Wednesday", "Thursday", "Friday",
		"Saturday"
	],
	months = [
		"January", "February", "March",
		"April", "May", "June", "July",
		"August", "September", "October",
		"November", "December"
	];

// Append a suffix to dates.
// Example: 23 => 23rd, 1 => 1st.
function nth (d) {
  if(d>3 && d<21) return 'th';
  switch (d % 10) {
        case 1:  return "st";
        case 2:  return "nd";
        case 3:  return "rd";
        default: return "th";
    }
}

// Create a string representation of the date.
function formatDate ( date ) {
   /* return weekdays[date.getDay()] + ", " +
        date.getDate() + nth(date.getDate()) + " " +
        months[date.getMonth()] + " " +
        date.getFullYear();*/
    return  months[date.getMonth()] + " " + date.getDate() + nth(date.getDate()) + ", " +
        date.getFullYear();
}

// Write a date as a pretty value.
function setDate( value ){
    $(this).html(formatDate(new Date(+value)));   
}

// Create a new date from a string, return as a timestamp.
function timestamp(str){
    return new Date(str).getTime();   
}

function changeDate(newDate){
	document.getElementById("dateDisplayer").innerHTML=formatDate(new Date(+newDate));
}

/*
Returns the currently selected date as ddmmyyyy
*/
function getCurrentlySelectedDate(){
	var datePicker = document.getElementById("datePicker");
	var currentDateObject = new Date(+datePicker.value);
	var date = currentDateObject.getDate();
	var currentDate = "";
	if(date < 10){
		currentDate += "0";
	}
	currentDate += date;
	var month = currentDateObject.getMonth();
	month++;
	if(month < 10){
		currentDate+= "0";
	}
	currentDate += month; 
	currentDate += currentDateObject.getFullYear();
	alert(currentDate);
	return currentDate;
}