import config, models

if __name__ == '__main__':
  config.registerParseApp()
  test_model = models.TestObject(sampleText="Hello there!")
  test_model.save()
