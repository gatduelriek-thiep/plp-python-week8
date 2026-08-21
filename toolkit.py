{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "abf3ae24-e9be-45fc-ad0b-13999571f954",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Friday\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Thurday\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Monday\n",
      "Which subject will you read on monday?  Chem\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Tuesday\n",
      "Which subject will you read on Tuesday?  Bio\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Wednesday\n",
      "Which subject will you read on Wednesday?  Histo\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Thursday\n",
      "Which subject will you read on Thursday?  Comp\n",
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Show\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chem\n",
      "Bio\n",
      "Histo\n",
      "Comp\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show  Saturday\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You rest well. Good bye !! See you again\n"
     ]
    }
   ],
   "source": [
    "# Start by creating the empty list\n",
    "to_do = []\n",
    "\n",
    "# Iterate through using while loop to check if the value for each day is correct\n",
    "\n",
    "while True:\n",
    "    \n",
    "    user = input(\"Choose what to do: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Show \")\n",
    "\n",
    "    if user == \"Monday\":\n",
    "        \n",
    "        action = input(\"Which subject will you read on monday? \") # From this code upto thursday ask the user to input the day and ask the student on\n",
    "        \n",
    "        to_do.append(action)\n",
    "                                                                    # Which subject to read on that day\n",
    "    elif user == \"Tuesday\":\n",
    "        \n",
    "        action = input(\"Which subject will you read on Tuesday? \")\n",
    "        \n",
    "        to_do.append(action)\n",
    "    \n",
    "    elif user == \"Wednesday\":\n",
    "        \n",
    "        action = input(\"Which subject will you read on Wednesday? \")\n",
    "        \n",
    "        to_do.append(action)\n",
    "    \n",
    "    elif user == \"Thursday\":\n",
    "        \n",
    "        action = input(\"Which subject will you read on Thursday? \")\n",
    "        \n",
    "        to_do.append(action)\n",
    "\n",
    "    elif user == \"Show\": # This program allow the student to check what to do each day in a week if he insert something to the prompt\n",
    "       \n",
    "        for a in to_do:\n",
    "            \n",
    "            print(a)\n",
    "    \n",
    "    elif user == \"Saturday\": # This code allow the student to rest by skipping the reading since it is a sabbath day\n",
    "        \n",
    "        print(\"You rest well. Good bye !! See you again\")\n",
    "        \n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db2d6cab-c96f-48ce-bb4f-ecfa00b9fed9",
   "metadata": {},
   "source": [
    "# Toolkit_plan.txt to explain the above project\n",
    "The purpose of the above project will be explain by the text file that I will create below using Python opening file with \"with statement\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a70b719-6fd9-4e65-b95e-0b690ebd5f5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Start with with statement since it will know how to deal with errors and close the file automatically when we are done with it\n",
    "with open(\"Desktop/toolkit_plan.txt\", \"w\") as file:\n",
    "    file_write = file.write(\"In the toolkit.py I use the concept we had covered before starting from foundation of Python\\n\"\n",
    "              \"Then data types like boolean, strings and data structure called list\\n\"\n",
    "              \"After that I move into concept of automation to allow computer to automate common and repetitive task in my project I use while loop\\n\"\n",
    "              \"After that I use print and input to make my project interactive\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1c660d99-e00d-4f9c-b839-82c9c1f84e5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In the toolkit.py I use the concept we had covered before starting from foundation of Python\n",
      "Then data types like boolean, strings and data structure called list\n",
      "After that I move into concept of automation to allow computer to automate common and repetitive task in my project I use while loop\n",
      "After that I use print and input to make my project interactive\n"
     ]
    }
   ],
   "source": [
    "with open(\"Desktop/toolkit_plan.txt\", \"r\") as file:\n",
    "    read_file = file.read()\n",
    "    print(read_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "935f7f4d-cb63-4602-a158-2eefd1fa16d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let me add details to my toolbox plan file using the append method\n",
    "with open(\"Desktop/toolkit_plan.txt\", \"a\") as file:\n",
    "    other_details = file.write(\"Incase if you want to give me a job as an instructor I know how to work well with other data structures like dictionary, sets and tuples\\n\"\n",
    "              \"I also know how to define and call the functions and pass some parameters and arguments to the functions as well as how to return information\\n\"\n",
    "              \"from return statement\"\n",
    "              \"I also have some working projects from Python libraries like pandas, numpy, matplotlib, beautifulsoup, regex, and selenium\\n\"\n",
    "              \"I am happy with this PLP project because it fosters hands-on practices which make someone do a lot of research in the evolving world of\\n\"\n",
    "              \"Computer programming\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7f4d9b32-e20a-4250-90db-b5858e12b2e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In the toolkit.py I use the concept we had covered before starting from foundation of Python\n",
      "Then data types like boolean, strings and data structure called list\n",
      "After that I move into concept of automation to allow computer to automate common and repetitive task in my project I use while loop\n",
      "After that I use print and input to make my project interactiveIncase if you want to give me a job as an instructor I know how to work well with other data structures like dictionary, sets and tuples\n",
      "I also know how to define and call the functions and pass some parameters and arguments to the functions as well as how to return information\n",
      "from return statementI also have some working projects from Python libraries like pandas, numpy, matplotlib, beautifulsoup, regex, and selenium\n",
      "I am happy with this PLP project because it fosters hands-on practices which make someone do a lot of research in the evolving world of\n",
      "Computer programming\n"
     ]
    }
   ],
   "source": [
    "with open(\"Desktop/toolkit_plan.txt\", \"r\") as file: # This with statement allow me to read what is in the text file\n",
    "    other_details = file.read()\n",
    "    print(other_details)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85385960-f59f-4992-9c56-13dc79c67580",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
