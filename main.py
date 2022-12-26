from Template import Template
from Entry import Entry

if __name__ == '__main__':
  e0 = Entry("Name", "Lancelot")
  e1 = Entry("Last Name", "Rey")
  e2 = Entry("Age", "43")

  t0 = Template()
  t0.addEntry(e0)
  t0.addEntry(e1)
  t0.addEntry(e2)

  print(t0)