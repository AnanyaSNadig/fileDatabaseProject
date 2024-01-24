import click, os, time, datetime

class Files:
    def __init__(self,path, timeFrame):
        self.path = path
        self.timeFrame = timeFrame

    def get(self, curPath = None, modifiedFiles = None):
        if curPath == None:
            curPath = self.path

        if modifiedFiles == None:
            modifiedFiles = []

        click.echo(f"Files in {curPath}")
        dir = sorted(os.listdir(curPath))

        for file in dir:
            new_path = os.path.join(curPath,file)

            if not os.path.isdir(new_path):
                click.echo(f"File: {file}")
                
                lastModified = os.path.getmtime(new_path)
                curTime = time.time()
                timeDiff = (curTime - lastModified)

                if timeDiff <= (self.timeFrame * 60):
                    modifiedFiles.append(new_path)

            else:
                if not os.listdir(new_path):
                    click.echo(f"Empty directory: {file}")
                
                else:
                    click.echo(f'\nDirectory: {file}')
                    self.get(new_path, modifiedFiles) 
                    click.echo() 

        return modifiedFiles  
    
    def update(self, filePath, searchStr, replaceStr):
        #TODO change to single file

        fileInfo = replacedTime = None

        for encoding in ['utf-8', 'ISO-8859-1', 'Windows-1252']:
            try:
                with open(filePath, 'r', encoding=encoding) as file:
                    fileInfo = file.read()
                break

            except UnicodeDecodeError:
                continue

        if fileInfo and searchStr in fileInfo:
            fileInfo = fileInfo.replace(searchStr, replaceStr)
            replacedTime = datetime.datetime.now()
            with open(filePath, 'w') as file:
                file.write(fileInfo)

        return filePath, searchStr, replaceStr, replacedTime
    