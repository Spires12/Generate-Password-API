from app import create_app

app = create_app()

def main():
  """ Function initialization project """
  app.run(debug=True)

if __name__ == '__main__':
  main()

