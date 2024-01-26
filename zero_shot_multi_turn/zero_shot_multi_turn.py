from pathlib import Path

from chatgpt4pcg.competition import chat_with_chatgpt, run_evaluation
from chatgpt4pcg.models.trial_context import TrialContext
from chatgpt4pcg.models.trial_loop import TrialLoop
from dotenv import load_dotenv


class ZeroShotMultiTurnPrompting(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        """
        Runs the zero-shot multi-turn prompting.
        :param ctx: The trial context.
        :param target_character: The target character.
        :return: The generated text.
        """
        prompts = [file for file in Path("prompts").glob("*.txt")]
        history = []
        for prompt in prompts:
            prompt_template = open(prompt, "r").read()
            history.append({"role": "user", "content": prompt_template.replace("<OBJECT>", target_character)})
            response = chat_with_chatgpt(ctx, history)
            response = response[0]
            history.append({"role": "assistant", "content": response})

        final_response = [item["content"] for item in history if item["role"] == "assistant"][-1]
        return final_response


if __name__ == "__main__":
    load_dotenv()
    run_evaluation("zero_shot_multi_turn", ZeroShotMultiTurnPrompting, num_trials=1, characters=["A"])
