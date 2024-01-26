from pathlib import Path

from chatgpt4pcg.competition import chat_with_chatgpt, run_evaluation
from chatgpt4pcg.models.trial_context import TrialContext
from chatgpt4pcg.models.trial_loop import TrialLoop
from dotenv import load_dotenv


class NullShotPrompting(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        """
        Runs the null-shot prompting.
        :param ctx: The trial context.
        :param target_character: The target character.
        :return: The generated text.
        """
        prompt_template = open(Path("prompts/null_shot.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        response = response[0]
        return response


if __name__ == "__main__":
    load_dotenv()
    run_evaluation("null_shot", NullShotPrompting, num_trials=1, characters=["A"])
