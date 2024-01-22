from pathlib import Path

from chatgpt4pcg.models.trial_loop import TrialLoop
from chatgpt4pcg.models.trial_context import TrialContext
from chatgpt4pcg.competition import chat_with_chatgpt, run_evaluation
from dotenv import load_dotenv


class ZeroShotPrompting(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        """
        Runs the zero-shot prompting.
        :param ctx: The trial context.
        :param target_character: The target character.
        :return: The generated text.
        """
        prompt_template = open(Path("prompts/zero_shot.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .format(target_character)}])

        return response


if __name__ == "__main__":
    load_dotenv()
    run_evaluation("example_prompting", ZeroShotPrompting, num_trials=1, characters=["A"])
