from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.App(__name__, port=9090, specification_dir='spec/')
    app.add_api('word_pyramid_api.yaml', resolver=RestyResolver('word_pyramid'))
    app.run()