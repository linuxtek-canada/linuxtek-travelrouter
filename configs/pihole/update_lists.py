#!/usr/bin/python3

import sqlite3
import docker
import subprocess

# Function to insert blacklists or whitelists into the Pi-hole database
def insert_adlist_to_db(domain_file, db_path, domain_type):
    """
    Inserts domains (blacklist or whitelist) into Pi-hole database gravity table.

    Parameters:
    - domain_file: Path to the file containing the list of domains (blacklist or whitelist).
    - db_path: Path to the Pi-hole SQLite database.
    - domain_type: Type of the domain (0 for blacklist, 1 for whitelist).
    """
    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read the domains from the file and insert them into the database
    with open(domain_file, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespaces and split the line by commas
            line = line.strip()

            # If the line is not empty, proceed to parse and insert it
            if line:
                # Handle the format: "URL",1,"Name" or "URL",1,Name
                parts = line.split(',', 2)

                # Ensure the line is correctly formatted
                if len(parts) == 3:
                    url = parts[0].strip('"')  # Remove the surrounding quotes
                    enabled = int(parts[1].strip())  # Convert the enabled flag to an integer
                    comment = parts[2].strip('"')  # Remove the surrounding quotes

                    # Insert the domain into the appropriate table (domainlist for whitelist)
                    cursor.execute('''
                    INSERT INTO adlist (address, enabled, comment)
                    VALUES (?, ?, ?)
                    ''', (url,enabled,comment))

    # Commit changes to the database
    conn.commit()

    # Close the connection
    conn.close()

    print(f"Domains (type {domain_type}) imported successfully into gravity.db!")

# Function to insert blacklists or whitelists into the Pi-hole database
def insert_explicit_domains_to_db(domain_file, db_path, domain_type):
    """
    Inserts explicit domains (blacklist or whitelist) into Pi-hole database.

    Parameters:
    - domain_file: Path to the file containing the list of domains (blacklist or whitelist).
    - db_path: Path to the Pi-hole SQLite database.
    - domain_type: Type of the domain (0 for blacklist, 1 for whitelist).
    """

    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read the domains from the file and insert them into the database
    with open(domain_file, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespaces and split the line by commas
            line = line.strip()

            # If the line is not empty, proceed to parse and insert it
            if line:
                # Handle the format: "URL",1,"Name" or "URL",1,Name
                parts = line.split(',', 2)

                # Ensure the line is correctly formatted
                if len(parts) == 3:
                    url = parts[0].strip('"')  # Remove the surrounding quotes
                    enabled = int(parts[1].strip())  # Convert the enabled flag to an integer
                    comment = parts[2].strip('"')  # Remove the surrounding quotes

                    # Insert the domain into the appropriate table (domainlist for whitelist)
                    cursor.execute('''
                    INSERT INTO domainlist (domain, enabled, comment)
                    VALUES (?, ?, ?)
                    ''', (url,enabled,comment))

    # Commit changes to the database
    conn.commit()

    # Close the connection
    conn.close()    

    print(f"Explicit domains (type {domain_type}) imported successfully into gravity.db!")

import subprocess

def update_gravity_in_pihole(container_name='pihole'):
    """
    Runs the 'pihole -g' command inside the Pi-hole Docker container to update gravity.
    
    Parameters:
    - container_name: The name of the Pi-hole Docker container (default is 'pihole').
    """
    try:
        # Docker exec command to run pihole -g inside the Pi-hole container
        command = ['docker', 'exec', container_name, 'pihole', '-g']

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Output the result of the command
        print("Gravity updated successfully!")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"Error updating gravity: {e}")
        print(f"stderr: {e.stderr}")

def main():
    # Path to the SQLite database (change it to your Pi-Hole gravity.db path if necessary)
    db_path = '/opt/docker/pihole/etc-pihole/gravity.db'
    container_name = 'pihole'

    # Path to the text files containing the blacklists and whitelists
    blacklist_file = 'blacklist.txt'
    whitelist_file = 'whitelist.txt'
    explicit_whitelist_file = 'explicit_whitelist.txt'
    explicit_blacklist_file = 'explicit_blacklist.txt'

    # Insert the blacklists into the adlist table
    print("Inserting blacklists...")
    insert_adlist_to_db(blacklist_file, db_path, 'blacklist')

    # Insert the whitelists into the adlist table
    print("Inserting whitelists...")
    insert_adlist_to_db(whitelist_file, db_path, 'whitelist')

    # Inserting explicit domains to whitelist
    print("Inserting explicit domain whitelists...")
    insert_explicit_domains_to_db(explicit_whitelist_file,db_path,'whitelist')

    # Inserting explicit domains to blacklist
    print("Inserting explicit domain blacklist...")
    insert_explicit_domains_to_db(explicit_blacklist_file,db_path,'blacklist')

    print("Updating gravity with all new lists and domains...")
    update_gravity_in_pihole('pihole')

if __name__ == "__main__":
    # Call the main function to insert the data
    main()