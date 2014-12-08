import model
import collect_info
import view
import datetime

class Controller(object):
    def __init__(self):
        view.welcome()
        self.evaluations()

    def evaluations(self):
        results = model.Evaluation.correct_percent(collect_info.websites)
        view.show_evaluations(results)
        non_margs = model.Evaluation.non_marginal_correct(collect_info.websites)
        choice = view.show_non_marginal(non_margs)
        if choice == "y":
            self.todays_predictions()
        else:
            return True

    def todays_predictions(self):
        predicts = model.Database.all_predicts_by_date(datetime.date.today())
        return view.show_todays(predicts)

    def consistent_winners(self):
        winners = model.Evaluation.consistent_winnners()
        view.show_consistent_winners(winners)


here = Controller()