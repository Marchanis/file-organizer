import os
import shutil #This module allows high-level file operations, such as moving files.



def organize_file(directory):
    categories = {
        'Image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents':['.pdf', '.doc', '.docx', '.txt','.xlsx','.pptx'],
        'Videos': ['.mp4','.avi', '.mov', '.mkv'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.gz'],
    }
    
    for category in categories :
        category_path = os.path.join(directory, category) #os.path.join() is used to create a file path that is valid across ops
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            
    
    #Create a Miscellaneous folder for uncategorized files
    misc_path = os.path.join(directory, 'Miscellaneous')
    if not os.path.exists(misc_path):
        os.makedirs(misc_path)

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, file_extension =os.path.splitext(filename)
            
            # Identify the category based on the file extension

            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    category_path= os.path.join(directory, category)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved: {filename} to {category}")
                    break
            else: 
                # Move uncategorized files to Miscellaneous
                shutil.move(file_path, os.path.join(misc_path, filename))
                print(f"Moved: {filename} to Miscellaneous")

                
    report = generate_report(directory, category)
    print("\nFille Organization Report: ")
    for category, data in report.items():
        print(f"{category}: {data['count']} files, {data['size']} bytes")
        
def generate_report(directory, categories):
    report = {}
    for category in categories:
        category_path = os.path.join(directory, category)
        total_size = 0
        file_count = 0
        
        #check if the category folder exists 
        if os.path.exists(category_path):
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
                    file_path += 1
        
        report[category] = {'size': total_size, 'count': file_count}
    
    
    # Check for Miscellaneous folder
    misc_path = os.path.join(directory, 'Miscellaneous')
    if os.path.exists(misc_path):
        total_size = 0
        file_count = 0
        for filename in os.listdir(misc_path):
            file_path = os.path.join(misc_path, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
                file_count += 1
        report['Miscellaneous'] = {'size': total_size, 'count': file_count}
    return report
    
    
                
if __name__ == "__main__":
    directory = input("Enter the directory to organize: ")
    if os.path.exists(directory):
        organize_file(directory)
    else:
        print('Invalid directory path!')