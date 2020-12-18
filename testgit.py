import cgitb

def testgit():
    try:
        import subprocess
    except Exception as e:
        print("%s error !"%e)
        return False
    else:
        return True
if __name__ == '__main__':
    testgit()