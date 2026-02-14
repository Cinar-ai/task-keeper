tasks = []
while True:
  print("\n1) Add task")
  print("2) Show task")
  print("3) Delete task")
  print("4) Exit")
  
  choice = input("Select: ")
  
  if choice == "1":
    task = input("Task: ")
    task.append(task)
    print("added")
    
  elif choice == "2":
    if not tasks:
      print("No tasks")
    else: 
      for i, t in enumerate(tasks, 1):
        print(f"{i}) {t}")
        
  elif choice == "3":
    try:
      num = int(input("Task number to delete: "))
      tasks.pop(num - 1)
      print("Deleted")
    except:
      print("Invalid input")
      
  elif choice == "4":
    break
  
  else:
    print("Invalid choice")
