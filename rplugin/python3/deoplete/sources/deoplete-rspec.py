import re
import traceback
from deoplete.source.base import Base

# ------------------------------- KEYWORD -------------------------------------------------------------------------
rspec_keywords = [
    'describe',
    'context',
    'it',
    'before',
    'after',
    'context',
    'example',
    'let',
    'let!',
    'expect',
    'expect_any_instance_of',
    'allow_any_instance_of',
    'to',
    'not_to',
    'to_not',
    'subject',
    'assert_select',
    'shared_examples',
    'include_examples',
    'it_behaves_like',
    'it_should_behave_like',
    'matching',
    'aggregate_failures',
    'all',
    'be',
    'be_a',
    'be_a_kind_of',
    'be_an_instance_of',
    'be_between',
    'be_falsey',
    'be_nil',
    'be_truthy',
    'be_within',
    'change',
    'contain_exactly',
    'cover',
    'end_with',
    'eq',
    'eql',
    'equal',
    'exist',
    'have_attributes',
    'include',
    'match',
    'match_array',
    'output',
    'raise_error',
    'respond_to',
    'satisfy',
    'start_with',
    'throw_symbol',
    'yield_control',
    'yield_successive_args',
    'yield_with_args',
    'yield_with_no_args',
    'a_value',
    'be_an',
    'be_kind_of',
    'a_kind_of',
    'be_instance_of',
    'an_instance_of',
    'a_value_between',
    'a_falsey_value',
    'a_nil_value',
    'a_truthy_value',
    'a_value_within',
    'within',
    'a_block_changing',
    'changing',
    'a_collection_containing_exactly',
    'containing_exactly',
    'a_range_covering',
    'covering',
    'a_collection_ending_with',
    'a_string_ending_with',
    'ending_with',
    'an_object_eq_to',
    'eq_to',
    'an_object_eql_to',
    'eql_to',
    'an_object_equal_to',
    'equal_to',
    'an_object_existing',
    'existing',
    'an_object_having_attributes',
    'having_attributes',
    'a_collection_including',
    'a_string_including',
    'a_hash_including',
    'including',
    'match_regex',
    'an_object_matching',
    'a_string_matching',
    'matching',
    'a_block_outputting',
    'a_block_raising',
    'raising',
    'an_object_responding_to',
    'responding_to',
    'an_object_satisfying',
    'satisfying',
    'a_collection_starting_with',
    'a_string_starting_with',
    'starting_with',
    'a_block_throwing',
    'throwing',
    'a_block_yielding_control',
    'yielding_control',
    'a_block_yielding_successive_args',
    'yielding_successive_args',
    'a_block_yielding_with_args',
    'yielding_with_args',
    'a_block_yielding_with_no_args',
    'yielding_with_no_args',
    'from',
    'by',
    'by_at_least',
    'by_at_most',
    'be_a_new',
    'render_template',
    'redirect_to',
    'route_to',
    'be_routable',
    'have_http_status',
    'match_array',
    'have_been_enqueued',
    'have_enqueued_job',
    'double',
    'instance_double',
    'receive',
    'receive_messages',
    'receive_message_chain',
    'and_return',
    'and_raise',
    'and_throw',
    'and_yield',
    'and_call_original',
    'spy',
    'instance_spy',
    'class_spy',
    'object_spy',
    'have_received',
    'with',
    'once',
    'twice',
    'exactly',
    'at_least',
    'at_most',
    'times',
    'ordered'
]
# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'deoplete-rspec'
        self.filetypes = ['ruby']
        self.mark = '[RSpec]'
        self.rank = 10

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = rspec_keywords
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
