#!/usr/bin/env python3
"""Minnesota SEL target repair pass (v1 -> v2).

Executes the repair brief (learnos-target-repair-brief-2026-07-06-v1.md) against
mn-sel-targets-2026-07-06-v1.json, governed by the measurement foundations v3.

Passes 1-5 are encoded as authored data below (per-target judgement made in
session, Opus). The script applies them deterministically, preserving provenance,
appends the 20 integrative targets, runs the Pass-5 sweep, and reports counts.
"""
import json, re, sys, collections

SRC = "minnesota-sel/output/mn-sel-targets-2026-07-06-v1.json"
OUT = "minnesota-sel/output/mn-sel-targets-2026-07-06-v2.json"

# --- Pass 1: remerge decision -------------------------------------------------
# Only sole-evidence pair (recognize/label) remerges; anchored on observable verb.
DROP = {"MN.SA.LG1.K-3.01-t02"}  # merged into -t01 ("name my emotions and feelings")

# --- Passes 2/3/5: per-target [statement, channel, modality] -------------------
# channel: ex=explain, do=do, both. modality: d=decided(compliant pass-through), p=proposed.
R = {
 # ===== SELF-AWARENESS =====
 "MN.SA.LG1.K-3.01-t01": ["I can name my emotions and feelings.", "explain", "p"],  # REMERGED
 "MN.SA.LG1.K-3.02-t01": ["I can identify positive and negative emotions.", "explain", "d"],
 "MN.SA.LG1.K-3.03-t01": ["I can identify emotions related to different situations or events.", "explain", "d"],
 "MN.SA.LG1.4-5.04-t01": ["I can use specific vocabulary to communicate my emotions and feelings.", "explain", "p"],
 "MN.SA.LG1.4-5.05-t01": ["I can distinguish degrees of my own emotional intensity.", "explain", "d"],
 "MN.SA.LG1.4-5.06-t01": ["I can describe the connection between my thoughts, emotions, and behaviors.", "explain", "p"],
 "MN.SA.LG1.4-5.07-t01": ["I can describe how I physically respond to emotion.", "explain", "d"],
 "MN.SA.LG1.6-8.08-t01": ["I can explain how an intense or mixed emotion can signal that a situation needs attention.", "explain", "p"],
 "MN.SA.LG1.6-8.09-t01": ["I can analyze which of my emotional states help or hinder my ability to problem-solve.", "explain", "p"],
 "MN.SA.LG1.6-8.10-t01": ["I can assess my emotional reactions in different contexts.", "explain", "p"],
 "MN.SA.LG1.9-12.11-t01": ["I can distinguish the emotions I hold from how others expect me to feel.", "explain", "d"],
 "MN.SA.LG1.9-12.12-t01": ["I can describe how external events or internal thoughts can trigger multiple emotions.", "explain", "d"],
 "MN.SA.LG1.9-12.13-t01": ["I can describe how changing my interpretation of an event can change how I feel about it.", "explain", "p"],
 "MN.SA.LG1.9-12.14-t01": ["I can assess whether the intensity of my emotions fits a given situation.", "explain", "p"],
 "MN.SA.LG1.9-12.15-t01": ["I can explain how identity and heritage practices shape the way I interpret emotions.", "explain", "p"],
 "MN.SA.LG2.K-3.01-t01": ["I can describe an activity or task in which I may need help to be successful.", "explain", "p"],
 "MN.SA.LG2.K-3.02-t01": ["I can identify family, peer, school, community, cultural, and linguistic strengths.", "explain", "d"],
 "MN.SA.LG2.4-5.03-t01": ["I can describe the personal strengths and assets that make me a successful member of my school and community.", "explain", "p"],
 "MN.SA.LG2.4-5.04-t01": ["I can identify opportunities to develop skills and talents.", "explain", "p"],
 "MN.SA.LG2.4-5.04-t02": ["I can explore opportunities to develop skills and talents.", "do", "p"],
 "MN.SA.LG2.4-5.05-t01": ["I can determine ways to use family, school, and community resources to accomplish tasks.", "explain", "d"],
 "MN.SA.LG2.6-8.06-t01": ["I can identify my strengths to meet a need or address a challenge.", "explain", "p"],
 "MN.SA.LG2.6-8.07-t01": ["I can identify an individual affinity or interest group.", "explain", "p"],
 "MN.SA.LG2.6-8.07-t02": ["I can enhance an individual affinity or interest group.", "do", "p"],
 "MN.SA.LG2.9-12.08-t01": ["I can evaluate my strengths and challenges in relation to achieving goals.", "explain", "p"],
 "MN.SA.LG2.9-12.09-t01": ["I can identify things about myself that I cannot change.", "explain", "p"],
 "MN.SA.LG2.9-12.09-t02": ["I can devote my energy to something I can change.", "do", "p"],
 "MN.SA.LG2.9-12.10-t01": ["I can analyze how my personal qualities contribute to my community and family.", "explain", "p"],
 "MN.SA.LG2.9-12.11-t01": ["I can examine how my actions create unjust imbalances in opportunity, access, participation, and success for particular groups.", "explain", "p"],
 "MN.SA.LG3.K-3.01-t01": ["I can describe what it feels like to feel safe and respected.", "explain", "d"],
 "MN.SA.LG3.K-3.02-t01": ["I can explain positive and negative consequences for my choices and actions.", "explain", "d"],
 "MN.SA.LG3.K-3.03-t01": ["I can take care of my own belongings.", "do", "p"],
 "MN.SA.LG3.K-3.04-t01": ["I can ask permission and take care when I use others' belongings.", "do", "p"],
 "MN.SA.LG3.4-5.05-t01": ["I can define my role in ensuring safety and respect for others.", "explain", "d"],
 "MN.SA.LG3.4-5.06-t01": ["I can accept positive or negative consequences of my own choices and actions.", "do", "p"],
 "MN.SA.LG3.4-5.07-t01": ["I can identify areas of personal responsibility.", "explain", "d"],
 "MN.SA.LG3.4-5.08-t01": ["I can explain the benefits of being responsible to myself and others.", "explain", "d"],
 "MN.SA.LG3.6-8.09-t01": ["I can assert my rights in a way that respects the rights of others.", "do", "p"],
 "MN.SA.LG3.6-8.10-t01": ["I can analyze the short- and long-term outcomes of choices and behavior.", "explain", "d"],
 "MN.SA.LG3.6-8.11-t01": ["I can identify areas of control I have over situations in life.", "explain", "d"],
 "MN.SA.LG3.6-8.12-t01": ["I can define my responsibility for the outcomes of safe, risky, or harmful behaviors.", "explain", "d"],
 "MN.SA.LG3.9-12.13-t01": ["I can advocate for the rights of myself and others.", "do", "d"],
 "MN.SA.LG3.9-12.14-t01": ["I can describe how taking personal responsibility can lead to success.", "explain", "d"],
 "MN.SA.LG3.9-12.15-t01": ["I can explain how much control I have over my own life.", "explain", "p"],
 "MN.SA.LG3.9-12.15-t02": ["I can act in line with how much control I have over my own life.", "do", "p"],
 # ===== SELF-MANAGEMENT =====
 "MN.SM.LG1.K-3.01-t01": ["I can use calming strategies to manage my emotions, thoughts, impulses, and stress.", "do", "p"],
 "MN.SM.LG1.K-3.02-t01": ["I can describe how feelings relate to thoughts and behaviors.", "explain", "d"],
 "MN.SM.LG1.K-3.03-t01": ["I can identify the choices I have in my behavior.", "explain", "p"],
 "MN.SM.LG1.K-3.04-t01": ["I can explain why it is important not to give up.", "explain", "p"],
 "MN.SM.LG1.4-5.05-t01": ["I can use coping skills to manage my emotions and behaviors.", "do", "p"],
 "MN.SM.LG1.4-5.06-t01": ["I can use constructive ways of expressing my emotions, thoughts, impulses, and stress.", "do", "p"],
 "MN.SM.LG1.4-5.07-t01": ["I can explain the causes and effects of my emotions, thoughts, impulses, stress, and distress.", "explain", "p"],
 "MN.SM.LG1.4-5.08-t01": ["I can adapt to and overcome obstacles by persevering.", "do", "p"],
 "MN.SM.LG1.4-5.09-t01": ["I can analyze the relationship between my own ethical values and my behavior.", "explain", "p"],
 "MN.SM.LG1.6-8.10-t01": ["I can apply strategies to manage stress.", "do", "d"],
 "MN.SM.LG1.6-8.11-t01": ["I can evaluate the role attitudes play in being successful.", "explain", "d"],
 "MN.SM.LG1.6-8.12-t01": ["I can evaluate how ethical values contribute to lifelong success and relationship building.", "explain", "p"],
 "MN.SM.LG1.6-8.13-t01": ["I can apply strategies to motivate my successful performance.", "do", "p"],
 "MN.SM.LG1.9-12.14-t01": ["I can practice strategies to recognize difficult emotions.", "do", "p"],
 "MN.SM.LG1.9-12.14-t02": ["I can practice strategies to cope with difficult emotions.", "do", "p"],
 "MN.SM.LG1.9-12.15-t01": ["I can incorporate personal management skills on a daily basis.", "do", "p"],
 "MN.SM.LG1.9-12.16-t01": ["I can evaluate how my behaviors influence the environment and society.", "explain", "d"],
 "MN.SM.LG1.9-12.17-t01": ["I can analyze whether I am behaving in line with my ethical values.", "explain", "p"],
 "MN.SM.LG1.9-12.17-t02": ["I can adjust my behavior to align with my ethical values.", "do", "p"],
 "MN.SM.LG2.9-12.01-t01": ["I can build strategies to overcome roadblocks.", "do", "p"],
 "MN.SM.LG2.K-3.02-t01": ["I can identify personal goals.", "explain", "p"],
 "MN.SM.LG2.K-3.03-t01": ["I can monitor progress towards my personal goals.", "do", "p"],
 "MN.SM.LG2.K-3.04-t01": ["I can describe the steps needed to achieve short-term goals.", "explain", "p"],
 "MN.SM.LG2.K-3.04-t02": ["I can implement the steps needed to achieve short-term goals.", "do", "p"],
 "MN.SM.LG2.K-3.05-t01": ["I can identify personal resources to achieve goals.", "explain", "d"],
 "MN.SM.LG2.K-3.06-t01": ["I can receive feedback.", "do", "p"],
 "MN.SM.LG2.K-3.06-t02": ["I can act on feedback.", "do", "p"],
 "MN.SM.LG2.4-5.07-t01": ["I can identify goals across multiple domains.", "explain", "p"],
 "MN.SM.LG2.4-5.08-t01": ["I can monitor progress toward goals across multiple domains.", "do", "d"],
 "MN.SM.LG2.4-5.09-t01": ["I can implement the steps necessary to achieve my goals.", "do", "d"],
 "MN.SM.LG2.4-5.10-t01": ["I can identify internal and external resources necessary to overcome obstacles in meeting goals.", "explain", "d"],
 "MN.SM.LG2.4-5.11-t01": ["I can actively engage in a feedback loop.", "do", "p"],
 "MN.SM.LG2.6-8.12-t01": ["I can connect goal-setting skills to academic, personal, and civic success.", "explain", "d"],
 "MN.SM.LG2.6-8.13-t01": ["I can monitor progress towards goals.", "do", "p"],
 "MN.SM.LG2.6-8.13-t02": ["I can adjust steps toward goals as needed.", "do", "p"],
 "MN.SM.LG2.6-8.14-t01": ["I can balance multiple goals.", "do", "p"],
 "MN.SM.LG2.6-8.14-t02": ["I can prioritize multiple goals.", "do", "p"],
 "MN.SM.LG2.6-8.15-t01": ["I can use internal and external resources to help achieve goals.", "do", "p"],
 "MN.SM.LG2.6-8.16-t01": ["I can filter feedback from adults and peers.", "do", "p"],
 "MN.SM.LG2.9-12.17-t01": ["I can set both medium- and longer-term goals.", "do", "p"],
 "MN.SM.LG2.9-12.18-t01": ["I can monitor progress toward medium- and longer-term goals.", "do", "p"],
 "MN.SM.LG2.9-12.18-t02": ["I can adjust my plan for medium- and longer-term goals as needed.", "do", "p"],
 "MN.SM.LG2.9-12.19-t01": ["I can identify action steps that connect my current goals with my future, long-term goals.", "explain", "d"],
 "MN.SM.LG2.9-12.20-t01": ["I can analyze feedback from multiple sources.", "explain", "p"],
 "MN.SM.LG2.9-12.20-t02": ["I can implement feedback from multiple sources.", "do", "p"],
 # ===== SOCIAL AWARENESS =====
 "MN.SOA.LG1.K-3.01-t01": ["I can identify a range of emotional expressions in others.", "explain", "p"],
 "MN.SOA.LG1.K-3.02-t01": ["I can explain that others may experience situations differently from me.", "explain", "p"],
 "MN.SOA.LG1.K-3.03-t01": ["I can anticipate others' reactions in response to a specific situation.", "explain", "d"],
 "MN.SOA.LG1.4-5.04-t01": ["I can identify how my behavior affects the emotions of others.", "explain", "d"],
 "MN.SOA.LG1.4-5.05-t01": ["I can demonstrate respect for others' perspectives and points of view.", "do", "d"],
 "MN.SOA.LG1.4-5.06-t01": ["I can identify verbal, physical, or situational cues that indicate how others may feel.", "explain", "d"],
 "MN.SOA.LG1.6-8.07-t01": ["I can analyze how my behavior affects the emotions of others.", "explain", "p"],
 "MN.SOA.LG1.6-8.07-t02": ["I can determine ways to adjust my behavior in response to how it affects others' emotions.", "explain", "p"],
 "MN.SOA.LG1.6-8.08-t01": ["I can summarize another's point of view.", "explain", "d"],
 "MN.SOA.LG1.6-8.09-t01": ["I can predict others' feelings and perspectives in different situations.", "explain", "p"],
 "MN.SOA.LG1.6-8.10-t01": ["I can identify the factors that impact how I am perceived by others.", "explain", "p"],
 "MN.SOA.LG1.9-12.11-t01": ["I can acknowledge the perspectives of those who hold different opinions.", "explain", "p"],
 "MN.SOA.LG1.9-12.12-t01": ["I can ask questions to explore another person's perspective.", "do", "p"],
 "MN.SOA.LG1.9-12.13-t01": ["I can compare multiple perspectives on an issue.", "explain", "d"],
 "MN.SOA.LG1.9-12.14-t01": ["I can identify a specific human or social need in my school or community.", "explain", "p"],
 "MN.SOA.LG1.9-12.14-t02": ["I can act on an identified human or social need in my school or community, alone or with others.", "do", "p"],
 "MN.SOA.LG1.9-12.15-t01": ["I can differentiate between the factual and emotional content of what a person says.", "explain", "d"],
 "MN.SOA.LG2.K-3.01-t01": ["I can describe ways that people are similar and different.", "explain", "d"],
 "MN.SOA.LG2.K-3.02-t01": ["I can describe positive qualities in others.", "explain", "d"],
 "MN.SOA.LG2.K-3.03-t01": ["I can use respectful language and actions when dealing with conflict or differences of opinion.", "do", "d"],
 "MN.SOA.LG2.4-5.04-t01": ["I can describe the benefits of others' personal qualities and why everyone should not be the same.", "explain", "p"],
 "MN.SOA.LG2.4-5.05-t01": ["I can offer alternative ways to address conflict or differences of opinion with peers.", "do", "p"],
 "MN.SOA.LG2.4-5.06-t01": ["I can identify contributions of different social and cultural groups.", "explain", "p"],
 "MN.SOA.LG2.4-5.07-t01": ["I can define stereotyping, discrimination, and prejudice.", "explain", "p"],
 "MN.SOA.LG2.4-5.07-t02": ["I can identify examples of stereotyping, discrimination, and prejudice.", "explain", "p"],
 "MN.SOA.LG2.6-8.08-t01": ["I can analyze how people of different groups can help one another.", "explain", "p"],
 "MN.SOA.LG2.6-8.08-t02": ["I can analyze how people of different groups can show appreciation for one another.", "explain", "p"],
 "MN.SOA.LG2.6-8.09-t01": ["I can describe ways that communities and cultures are similar and different.", "explain", "d"],
 "MN.SOA.LG2.6-8.10-t01": ["I can explain how similarities and differences in cultural norms and social cues affect the way people interact.", "explain", "p"],
 "MN.SOA.LG2.6-8.11-t01": ["I can explain how the decisions and behaviors of individuals affect the well-being of schools or communities.", "explain", "d"],
 "MN.SOA.LG2.9-12.12-t01": ["I can demonstrate respect for individuals from different social and cultural groups.", "do", "d"],
 "MN.SOA.LG2.9-12.13-t01": ["I can explain apparent and not-apparent community and cultural practices, customs, and ways of making meaning that impact communities differently.", "explain", "p"],
 "MN.SOA.LG2.9-12.14-t01": ["I can explain how stereotyping, prejudice, and discrimination affect the design of institutions and social structures.", "explain", "p"],
 "MN.SOA.LG3.K-3.01-t01": ["I can identify responsibilities that contribute to my classroom.", "explain", "p"],
 "MN.SOA.LG3.K-3.01-t02": ["I can carry out responsibilities that contribute to my classroom.", "do", "p"],
 "MN.SOA.LG3.K-3.02-t01": ["I can identify how I help others.", "explain", "p"],
 "MN.SOA.LG3.K-3.03-t01": ["I can express how I feel when I help others.", "explain", "d"],
 "MN.SOA.LG3.4-5.04-t01": ["I can identify tasks that contribute to my school and community.", "explain", "p"],
 "MN.SOA.LG3.4-5.04-t02": ["I can perform tasks that contribute to my school and community.", "do", "p"],
 "MN.SOA.LG3.6-8.05-t01": ["I can explain how individual attitudes and behaviors affect the well-being of my school or community.", "explain", "d"],
 "MN.SOA.LG3.6-8.06-t01": ["I can describe a social movement, its leaders, and its strategies.", "explain", "p"],
 "MN.SOA.LG3.6-8.07-t01": ["I can work collaboratively with peers to analyze a shared school initiative.", "both", "p"],
 "MN.SOA.LG3.6-8.07-t02": ["I can work collaboratively with peers to address a shared school initiative.", "do", "p"],
 "MN.SOA.LG3.9-12.08-t01": ["I can work collaboratively with peers to analyze a shared social cause.", "both", "p"],
 "MN.SOA.LG3.9-12.08-t02": ["I can work collaboratively with peers to address a shared social cause.", "do", "p"],
 "MN.SOA.LG3.9-12.09-t01": ["I can analyze the impact of my involvement in an activity to improve my school or community.", "explain", "d"],
 "MN.SOA.LG4.K-3.01-t01": ["I can identify an adult I can trust.", "explain", "d"],
 "MN.SOA.LG4.K-3.02-t01": ["I can explain situations when I may need help.", "explain", "d"],
 "MN.SOA.LG4.K-3.03-t01": ["I can identify how and where to get help in an emergency situation.", "explain", "p"],
 "MN.SOA.LG4.4-5.04-t01": ["I can identify qualities of positive peer and adult role models.", "explain", "p"],
 "MN.SOA.LG4.4-5.05-t01": ["I can distinguish situations when I need support from situations when I do not.", "explain", "p"],
 "MN.SOA.LG4.4-5.06-t01": ["I can explain how family members, peers, school personnel, and community members can support school success and responsible behavior.", "explain", "d"],
 "MN.SOA.LG4.6-8.07-t01": ["I can apply qualities of positive peer and adult role models to myself.", "do", "d"],
 "MN.SOA.LG4.6-8.08-t01": ["I can identify a situation when I needed support but did not ask for it.", "explain", "p"],
 "MN.SOA.LG4.6-8.09-t01": ["I can analyze whether peers, school, and community members are supportive or non-supportive in accomplishing goals.", "explain", "d"],
 "MN.SOA.LG4.9-12.10-t01": ["I can seek out peer and adult role models who will help me achieve goals.", "do", "d"],
 "MN.SOA.LG4.9-12.11-t01": ["I can access family, peer, school, and community resources when support is needed.", "do", "d"],
 "MN.SOA.LG4.9-12.12-t01": ["I can build systems of support that contribute to school and personal success.", "do", "p"],
 # ===== RELATIONSHIP SKILLS =====
 "MN.RS.LG1.K-3.01-t01": ["I can take turns with others.", "do", "p"],
 "MN.RS.LG1.K-3.01-t02": ["I can share with others.", "do", "p"],
 "MN.RS.LG1.K-3.02-t01": ["I can use facial expressions, body language, and tone to communicate thoughts, feelings, emotions, and intentions.", "do", "p"],
 "MN.RS.LG1.K-3.03-t01": ["I can share genuine encouraging comments to support peers.", "do", "p"],
 "MN.RS.LG1.K-3.04-t01": ["I can listen when others are speaking.", "do", "d"],
 "MN.RS.LG1.4-5.05-t01": ["I can explain how groups behave differently than individuals and affect a person's emotions, attitudes, and behaviors.", "explain", "p"],
 "MN.RS.LG1.4-5.06-t01": ["I can explain how facial expressions, body language, and tone impact interactions.", "explain", "p"],
 "MN.RS.LG1.4-5.07-t01": ["I can demonstrate different ways to provide feedback to peers.", "do", "d"],
 "MN.RS.LG1.4-5.08-t01": ["I can use attentive listening skills to support communication.", "do", "p"],
 "MN.RS.LG1.6-8.09-t01": ["I can explain the different roles in a group and how these roles contribute to failure or success in group efforts.", "explain", "p"],
 "MN.RS.LG1.6-8.10-t01": ["I can monitor how facial expressions, body language, and tone impact interactions.", "do", "d"],
 "MN.RS.LG1.6-8.11-t01": ["I can respond with positive action steps from feedback.", "do", "p"],
 "MN.RS.LG1.6-8.12-t01": ["I can differentiate between passive, assertive, and aggressive responses from others.", "explain", "d"],
 "MN.RS.LG1.9-12.13-t01": ["I can create positive group dynamics to move group efforts forward.", "do", "d"],
 "MN.RS.LG1.9-12.14-t01": ["I can apply non-verbal skills to create productive outcomes during positive and negative interactions.", "do", "d"],
 "MN.RS.LG1.9-12.15-t01": ["I can adapt to different contexts, audiences, tasks, and feedback from myself and others.", "do", "p"],
 "MN.RS.LG2.9-12.01-t01": ["I can use assertive communication to get my needs met without negatively impacting others.", "do", "d"],
 "MN.RS.LG2.K-3.02-t01": ["I can describe how relationships differ from one another.", "explain", "p"],
 "MN.RS.LG2.K-3.03-t01": ["I can identify the qualities others have that I would like to see in myself.", "explain", "p"],
 "MN.RS.LG2.K-3.04-t01": ["I can build positive peer relationships based on shared activities and interests.", "do", "p"],
 "MN.RS.LG2.4-5.05-t01": ["I can describe the difference between positive and negative relationships.", "explain", "p"],
 "MN.RS.LG2.4-5.05-t02": ["I can identify behaviors that contribute to positive and negative relationships.", "explain", "p"],
 "MN.RS.LG2.4-5.06-t01": ["I can describe the value of friendships with different individuals.", "explain", "p"],
 "MN.RS.LG2.4-5.07-t01": ["I can identify a problem in a relationship.", "explain", "p"],
 "MN.RS.LG2.4-5.07-t02": ["I can seek assistance for a relationship problem.", "do", "p"],
 "MN.RS.LG2.4-5.08-t01": ["I can engage in cooperative learning and work toward group learning goals with peers.", "do", "p"],
 "MN.RS.LG2.4-5.09-t01": ["I can distinguish between positive and negative peer pressure.", "explain", "d"],
 "MN.RS.LG2.6-8.10-t01": ["I can demonstrate strategies for resisting negative peer pressure.", "do", "d"],
 "MN.RS.LG2.6-8.11-t01": ["I can identify ways to be involved in constructive, prosocial activities with others.", "explain", "p"],
 "MN.RS.LG2.6-8.11-t02": ["I can demonstrate ways to be involved in constructive, prosocial activities with others.", "do", "p"],
 "MN.RS.LG2.6-8.12-t01": ["I can explain the potential consequences of safe and unsafe behaviors in relationships.", "explain", "p"],
 "MN.RS.LG2.6-8.13-t01": ["I can build supportive relationships with peers.", "do", "p"],
 "MN.RS.LG2.9-12.14-t01": ["I can build romantic and non-romantic relationships with peers that are supportive and stable over time.", "do", "p"],
 "MN.RS.LG2.9-12.15-t01": ["I can identify the qualities and benefits of someone who is or might be a mentor.", "explain", "d"],
 "MN.RS.LG2.9-12.16-t01": ["I can provide leadership in cooperative learning.", "do", "p"],
 "MN.RS.LG3.K-3.01-t01": ["I can describe what conflict is.", "explain", "p"],
 "MN.RS.LG3.K-3.01-t02": ["I can describe feelings associated with conflict.", "explain", "p"],
 "MN.RS.LG3.K-3.02-t01": ["I can explain the other person's point of view when there is conflict.", "explain", "p"],
 "MN.RS.LG3.K-3.03-t01": ["I can identify potential solutions to a conflict.", "explain", "d"],
 "MN.RS.LG3.4-5.04-t01": ["I can identify conflicts as a natural part of life.", "explain", "d"],
 "MN.RS.LG3.4-5.05-t01": ["I can state a problem from multiple perspectives.", "explain", "p"],
 "MN.RS.LG3.4-5.06-t01": ["I can identify solutions to interpersonal conflict that meet the needs of myself and others.", "explain", "d"],
 "MN.RS.LG3.4-5.07-t01": ["I can state a problem using I-statements.", "do", "p"],
 "MN.RS.LG3.4-5.08-t01": ["I can explain the difference between my intent and the impact of my actions and words.", "explain", "p"],
 "MN.RS.LG3.6-8.09-t01": ["I can reflect on my role in conflict.", "explain", "d"],
 "MN.RS.LG3.6-8.10-t01": ["I can identify how a conflict can be resolved so everyone's needs are met.", "explain", "p"],
 "MN.RS.LG3.6-8.11-t01": ["I can apply conflict resolution skills to de-escalate, defuse, and resolve differences.", "do", "d"],  # BOUNDARY: kept single
 "MN.RS.LG3.6-8.12-t01": ["I can identify positive support people to seek out in a conflict situation.", "explain", "d"],
 "MN.RS.LG3.9-12.13-t01": ["I can evaluate and reflect on my role in a conflict.", "explain", "p"],
 "MN.RS.LG3.9-12.13-t02": ["I can use reflection on my role in a conflict to inform my future behavior.", "do", "p"],
 "MN.RS.LG3.9-12.14-t01": ["I can co-exist civilly in the face of unresolved conflict.", "do", "p"],
 "MN.RS.LG3.9-12.15-t01": ["I can access conflict resolution resources.", "do", "d"],
 "MN.RS.LG3.9-12.16-t01": ["I can describe negotiation skills.", "explain", "p"],
 "MN.RS.LG3.9-12.16-t02": ["I can apply negotiation skills.", "do", "p"],
 # ===== RESPONSIBLE DECISION-MAKING =====
 "MN.RDM.LG1.K-3.01-t01": ["I can identify shared bus, classroom, and school norms.", "explain", "p"],
 "MN.RDM.LG1.K-3.01-t02": ["I can follow shared bus, classroom, and school norms.", "do", "p"],
 "MN.RDM.LG1.K-3.02-t01": ["I can identify safe and unsafe behaviors.", "explain", "p"],
 "MN.RDM.LG1.K-3.02-t02": ["I can illustrate safe and unsafe behaviors.", "do", "p"],
 "MN.RDM.LG1.K-3.03-t01": ["I can explain that decisions can have positive and negative effects on me and others.", "explain", "p"],
 "MN.RDM.LG1.4-5.04-t01": ["I can contribute to school safety by supporting shared classroom, lunchroom, and playground norms and rules.", "do", "d"],
 "MN.RDM.LG1.4-5.05-t01": ["I can identify ways certain decisions or choices affect short- and long-term goals.", "explain", "p"],
 "MN.RDM.LG1.4-5.06-t01": ["I can identify positive and negative consequences of decisions for myself and others.", "explain", "d"],
 "MN.RDM.LG1.6-8.07-t01": ["I can analyze the reasons for school rules and local laws.", "explain", "p"],
 "MN.RDM.LG1.6-8.07-t02": ["I can identify the ethical values and social norms that school rules and local laws support.", "explain", "p"],
 "MN.RDM.LG1.6-8.08-t01": ["I can monitor how my decision-making affects progress toward achieving a goal.", "do", "p"],
 "MN.RDM.LG1.6-8.09-t01": ["I can explain the effect of peer pressure on decision-making.", "explain", "p"],
 "MN.RDM.LG1.9-12.10-t01": ["I can consider personal responsibility, social norms, safety concerns, and ethical standards when making decisions.", "do", "p"],
 "MN.RDM.LG1.9-12.11-t01": ["I can assess lessons learned from past experiences and mistakes when making decisions.", "do", "d"],
 "MN.RDM.LG2.K-3.01-t01": ["I can implement the Stop, Think, and Act strategy when making decisions.", "do", "p"],
 "MN.RDM.LG2.K-3.02-t01": ["I can demonstrate cooperation with social and classroom norms and procedures.", "do", "d"],
 "MN.RDM.LG2.K-3.03-t01": ["I can explain the consequences and rewards of actions on myself, others, or a group.", "explain", "p"],
 "MN.RDM.LG2.4-5.04-t01": ["I can identify different decisions or problems that I have at school.", "explain", "p"],
 "MN.RDM.LG2.4-5.05-t01": ["I can generate alternative solutions to problems I have identified.", "explain", "p"],
 "MN.RDM.LG2.4-5.06-t01": ["I can assess the consequences of possible solutions to the identified problems.", "explain", "p"],
 "MN.RDM.LG2.4-5.06-t02": ["I can demonstrate methods for reaching consensus or a decision.", "do", "p"],
 "MN.RDM.LG2.4-5.07-t01": ["I can evaluate the results of my actions after making a decision.", "explain", "d"],
 "MN.RDM.LG2.6-8.08-t01": ["I can identify the steps of systematic decision-making.", "explain", "p"],
 "MN.RDM.LG2.6-8.08-t02": ["I can apply the steps of systematic decision-making, using creativity and innovation.", "do", "p"],
 "MN.RDM.LG2.6-8.09-t01": ["I can gather additional information from multiple sources to generate alternative solutions.", "do", "d"],
 "MN.RDM.LG2.6-8.10-t01": ["I can discuss alternatives in relation to multiple contextual factors.", "explain", "d"],
 "MN.RDM.LG2.6-8.11-t01": ["I can analyze how decision-making skills affect study habits and academic performance.", "explain", "d"],
 "MN.RDM.LG2.9-12.12-t01": ["I can regularly demonstrate use of systematic decision-making.", "do", "p"],
 "MN.RDM.LG2.9-12.13-t01": ["I can identify systematic questions that clarify different points of view and lead to the best solution.", "explain", "p"],
 "MN.RDM.LG2.9-12.13-t02": ["I can ask systematic questions that clarify different points of view and lead to the best solution.", "do", "p"],
 "MN.RDM.LG2.9-12.14-t01": ["I can analyze and evaluate evidence, arguments, claims, and beliefs to inform decisions.", "explain", "p"],  # BOUNDARY: kept single
 "MN.RDM.LG2.9-12.15-t01": ["I can analyze how my present decision-making affects college and career choices.", "explain", "d"],
}

# --- Pass 4: integrative targets (5 competencies x 4 bands) --------------------
BANDS = ["Band 1 (K–3)", "Band 2 (Grades 4–5)", "Band 3 (Grades 6–8)", "Band 4 (Grades 9–12)"]
BAND_CODE = {"Band 1 (K–3)": "B1", "Band 2 (Grades 4–5)": "B2", "Band 3 (Grades 6–8)": "B3", "Band 4 (Grades 9–12)": "B4"}
COMP_CODE = {"Self-Awareness": "SA", "Self-Management": "SM", "Social Awareness": "SOA",
             "Relationship Skills": "RS", "Responsible Decision-Making": "RDM"}
INTEGRATIVE = {
 "Self-Awareness": {
   "Band 1 (K–3)": "I can notice a feeling as it arises, name it, and say what may have caused it, during a real classroom moment.",
   "Band 2 (Grades 4–5)": "I can, in the middle of a challenging task, name what I am feeling, identify a personal strength I can draw on, and say how I will use it.",
   "Band 3 (Grades 6–8)": "I can, during a difficult situation, notice my emotional state, judge whether its intensity fits the situation, and describe the choices I still control.",
   "Band 4 (Grades 9–12)": "I can, in a real setback, name my emotions, separate what I can change from what I cannot, and direct my effort toward what I can change.",
 },
 "Self-Management": {
   "Band 1 (K–3)": "I can, when I feel upset during an activity, choose and use a calming strategy and return to the task.",
   "Band 2 (Grades 4–5)": "I can set a goal, carry out the steps toward it, and use a coping skill to keep going when I meet an obstacle.",
   "Band 3 (Grades 6–8)": "I can pursue a goal over several weeks, monitor my progress, and adjust my steps when feedback or setbacks call for it.",
   "Band 4 (Grades 9–12)": "I can manage a medium-term goal by planning steps, tracking progress, applying feedback from several sources, and adjusting my plan as needed.",
 },
 "Social Awareness": {
   "Band 1 (K–3)": "I can, during a group activity, notice how a classmate is feeling and change what I do to help that classmate take part.",
   "Band 2 (Grades 4–5)": "I can, in a disagreement with peers, describe another person's point of view and offer a respectful way to move forward.",
   "Band 3 (Grades 6–8)": "I can work with peers to understand a shared school issue, take others' perspectives into account, and act together to address it.",
   "Band 4 (Grades 9–12)": "I can identify a human or social need in my school or community, understand the perspectives of those affected, and act with others to address it.",
 },
 "Relationship Skills": {
   "Band 1 (K–3)": "I can take turns, listen while others speak, and use kind words to keep a shared activity going with a peer.",
   "Band 2 (Grades 4–5)": "I can, when a conflict arises with a peer, state the problem using I-statements and work with that peer toward a solution that meets both our needs.",
   "Band 3 (Grades 6–8)": "I can use assertive communication and conflict-resolution skills to de-escalate a disagreement and reach a win-win with a peer.",
   "Band 4 (Grades 9–12)": "I can build and maintain a supportive relationship, and when conflict arises, negotiate and co-exist civilly even when it stays unresolved.",
 },
 "Responsible Decision-Making": {
   "Band 1 (K–3)": "I can, when facing a choice, stop and think, follow the shared norms, and act in a way that is safe for me and others.",
   "Band 2 (Grades 4–5)": "I can name a real problem I face at school, generate solutions, weigh the consequences, and choose one together with others.",
   "Band 3 (Grades 6–8)": "I can apply the steps of systematic decision-making to a real problem, gathering information and weighing alternatives against ethical values and norms.",
   "Band 4 (Grades 9–12)": "I can make a real decision by gathering evidence from multiple sources, evaluating it, weighing it against ethical standards, and reflecting on the outcome.",
 },
}

CH = {"ex": "explain", "explain": "explain", "do": "do", "both": "both"}

def main():
    d = json.load(open(SRC))
    src_targets = d["targets"]
    # integrity: every kept id must be in R; R must not contain unknown ids
    kept_ids = [t["target_id"] for t in src_targets if t["target_id"] not in DROP]
    missing = [i for i in kept_ids if i not in R]
    extra = [i for i in R if i not in set(t["target_id"] for t in src_targets)]
    if missing: sys.exit(f"MISSING rewrites for: {missing}")
    if extra: sys.exit(f"UNKNOWN ids in R: {extra}")

    out_targets = []
    counts = collections.Counter()
    for t in src_targets:
        tid = t["target_id"]
        if tid in DROP:
            counts["remerged_dropped"] += 1
            continue
        stmt, chan, mod = R[tid]
        was_derived = "derived" in t.get("flags", [])
        # count classification
        if tid == "MN.SA.LG1.K-3.01-t01":
            counts["remerged_kept"] += 1
        if mod == "p":
            counts["rewritten"] += 1
        else:
            counts["already_canonical"] += 1
        if was_derived:
            counts["derived_kept_split"] += 1
        nt = dict(t)  # preserve every existing field (provenance untouched)
        nt["statement"] = stmt
        nt["word_count"] = len(stmt.split())
        nt["channel"] = CH[chan]
        nt["integrative"] = False
        nt["modality"] = "proposed" if mod == "p" else "decided"
        out_targets.append(nt)

    # append integrative targets
    for comp in ["Self-Awareness", "Self-Management", "Social Awareness", "Relationship Skills", "Responsible Decision-Making"]:
        for band in BANDS:
            stmt = INTEGRATIVE[comp][band]
            tid = f"LEARNOS.INT.{COMP_CODE[comp]}.{BAND_CODE[band]}-t01"
            out_targets.append({
                "statement": stmt,
                "type": 0,
                "knowledge_type": "",
                "assessment_route": "",
                "kud_source": "",
                "word_count": len(stmt.split()),
                "flags": ["integrative"],
                "lt_statement_format": "",
                "source_provenance": [],
                "kud_provenance": [],
                "source_benchmark_id": "",
                "source_verbatim": "",
                "casel_competency": comp,
                "casel_secondary": "",
                "developmental_band": band,
                "channel": "do",
                "integrative": True,
                "strategy_links": [],
                "modality": "proposed",
                "target_id": tid,
                "provenance": {
                    "source": "learnos-integrative",
                    "note": "Authored integrative target — no Minnesota benchmark. Whole-situation performance requiring this competency's components in concert (foundations v3 §8.4). Strategy links left empty for Kari.",
                    "casel_competency": comp,
                    "developmental_band": band,
                },
            })
            counts["integrative"] += 1

    d2 = dict(d)
    d2["version"] = "v2"
    d2["run"] = "Repair pass (learnos-target-repair-brief-2026-07-06-v1); Passes 1-5 inline Opus"
    d2["generated"] = "2026-07-06"
    d2["targets_total"] = len(out_targets)
    d2["targets"] = out_targets
    d2["repair_note"] = ("v2 = assessability re-split (1 remerge, 33 kept-split), canonical I-can rewrite, "
                         "channel affinity (explain/do/both), 20 integrative targets, vague-modifier sweep. "
                         "Governing doc: learnos-measurement-foundations-2026-07-06-v3.md.")
    json.dump(d2, open(OUT, "w"), indent=2, ensure_ascii=False)
    print("WROTE", OUT, "targets:", len(out_targets))
    print("COUNTS:", dict(counts))

if __name__ == "__main__":
    main()
