from app import create_app, db

from app.models import Message


if __name__ == '__main__':
    application = create_app()

    @application.shell_context_processor
    def make_shell_context():
        return dict(db=db, Message=Message)


    application.run(debug=True)