# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------


mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills): ### because we use here (dict) we should use this sign(**)



  for skill_kays,  skill_value in skills.items():

    print(f"{skill_kays} => { skill_value}")

show_skills(**mySkills)