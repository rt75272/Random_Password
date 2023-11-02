from termcolor import colored
import password

# Outputs cyan colored randomly generated password to terminal.
def main():
    psswrd = password.get_password()
    print(colored(psswrd, "cyan", attrs=['bold']))

main()